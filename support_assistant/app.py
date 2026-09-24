from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.graph import support_graph


app = FastAPI(
    title="Zepto Support Assistant",
    description="Offline-first Zepto policy support assistant",
    version="1.0.0"
)


class SupportResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: float = Field(
        ge=0.0,
        le=1.0
    )


class AskRequest(BaseModel):
    query: str


@app.post("/ask", response_model=SupportResponse)
def ask(request: AskRequest):
    graph_result = support_graph.invoke({
        "query": request.query
    })

    response = SupportResponse(
        answer=graph_result["answer"],
        sources=graph_result["sources"],
        confidence=graph_result["confidence"]
    )

    return response