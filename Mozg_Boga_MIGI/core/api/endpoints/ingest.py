from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter()

class Document(BaseModel):
    title: str
    content: str

documents_db = {}

@router.post("/v1/ingest", response_model=dict)
async def ingest_document(doc: Document):
    doc_id = str(uuid.uuid4())
    documents_db[doc_id] = {
        "title": doc.title,
        "content": doc.content
    }
    return {"doc_id": doc_id, "message": "Document ingested successfully."}

@router.get("/v1/ingest/{doc_id}", response_model=dict)
async def get_document(doc_id: str):
    if doc_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents_db[doc_id]