from pathlib import Path
from typing import TypedDict

import chromadb
from sentence_transformers import SentenceTransformer
from langgraph.graph import StateGraph, END


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"


class SupportState(TypedDict, total=False):
    query: str
    intent: str
    retrieved_chunks: list
    answer: str
    sources: list[str]
    confidence: float


POLICY_KEYWORDS = [
    "delivery",
    "return",
    "refund",
    "membership",
    "tracking",
    "cancel",
    "gift card",
    "support hours"
]


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = chroma_client.get_or_create_collection(
    name="zepto_policies",
    metadata={"hnsw:space": "cosine"}
)


def classify_intent(state: SupportState) -> SupportState:
    query = state["query"].lower()

    if any(keyword in query for keyword in POLICY_KEYWORDS):
        return {"intent": "policy_question"}

    return {"intent": "general_question"}


def retrieve_and_answer(state: SupportState) -> SupportState:
    query = state["query"]

    query_embedding = embedding_model.encode(
        [query],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    documents = results.get("documents", [[]])[0]
    ids = results.get("ids", [[]])[0]

    retrieved_chunks = [
        {
            "id": chunk_id,
            "text": document
        }
        for chunk_id, document in zip(ids, documents)
    ]

    if retrieved_chunks:
        answer = (
            "Based on the retrieved context: "
            + retrieved_chunks[0]["text"]
        )
        sources = ids
        confidence = 1.0
    else:
        answer = "I could not find relevant information in the policy documents."
        sources = []
        confidence = 0.0

    return {
        "retrieved_chunks": retrieved_chunks,
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }


def direct_answer(state: SupportState) -> SupportState:
    return {
        "answer": "I can only answer questions about Zepto policies right now.",
        "sources": [],
        "confidence": 1.0
    }


def route_after_classification(state: SupportState) -> str:
    if state["intent"] == "policy_question":
        return "retrieve_and_answer"

    return "direct_answer"


graph_builder = StateGraph(SupportState)

graph_builder.add_node("classify_intent", classify_intent)
graph_builder.add_node("retrieve_and_answer", retrieve_and_answer)
graph_builder.add_node("direct_answer", direct_answer)

graph_builder.set_entry_point("classify_intent")

graph_builder.add_conditional_edges(
    "classify_intent",
    route_after_classification,
    {
        "retrieve_and_answer": "retrieve_and_answer",
        "direct_answer": "direct_answer"
    }
)

graph_builder.add_edge("retrieve_and_answer", END)
graph_builder.add_edge("direct_answer", END)

support_graph = graph_builder.compile()
