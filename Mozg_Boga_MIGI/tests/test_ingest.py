import pytest
from core.api.endpoints.ingest import ingest_document

def test_ingest_valid_document():
    # Given a valid document
    document = {
        "title": "Test Document",
        "content": "This is a test document for ingestion."
    }
    
    # When the document is ingested
    response = ingest_document(document)
    
    # Then the response should indicate success
    assert response["status"] == "success"
    assert response["doc_id"] is not None

def test_ingest_missing_title():
    # Given a document with a missing title
    document = {
        "content": "This document is missing a title."
    }
    
    # When the document is ingested
    response = ingest_document(document)
    
    # Then the response should indicate failure
    assert response["status"] == "failure"
    assert "title" in response["errors"]

def test_ingest_empty_content():
    # Given a document with empty content
    document = {
        "title": "Empty Content Document",
        "content": ""
    }
    
    # When the document is ingested
    response = ingest_document(document)
    
    # Then the response should indicate failure
    assert response["status"] == "failure"
    assert "content" in response["errors"]