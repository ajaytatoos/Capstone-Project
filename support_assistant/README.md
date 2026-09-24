
# Zepto Support Assistant

An offline-first policy support assistant built with Sentence Transformers, ChromaDB, LangGraph, FastAPI, and Pydantic.

## Features

- Zepto policy document retrieval
- Sentence Transformer embeddings
- ChromaDB vector database
- Cosine similarity search
- LangGraph routing
- Pydantic response validation
- FastAPI `/ask` endpoint
- Deterministic offline baseline
- Docker support

## Project Structure

support_assistant/
├── docs/
│   ├── doc_01.txt
│   ├── doc_02.txt
│   ├── doc_03.txt
│   ├── doc_04.txt
│   ├── doc_05.txt
│   ├── doc_06.txt
│   ├── doc_07.txt
│   └── doc_08.txt
├── prompts/
│   └── structured_prompt.txt
├── src/
│   └── graph.py
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md

## Run Locally

Install dependencies:

    pip install -r requirements.txt

Start the API:

    uvicorn app:app --host 0.0.0.0 --port 8000

## API

### POST /ask

Example request:

    {
      "query": "How long do approved refunds take?"
    }

Example response:

    {
      "answer": "Based on the retrieved context: ...",
      "sources": [
        "doc_02_chunk_01"
      ],
      "confidence": 1.0
    }

## Offline Baseline

The project supports a deterministic offline baseline and does not require an external API key.

Default mode:

    MOCK_LLM=1

## Technology

- Python
- FastAPI
- Pydantic
- Sentence Transformers
- ChromaDB
- LangGraph
- LangChain
