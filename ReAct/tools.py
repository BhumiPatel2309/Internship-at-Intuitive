def load_document(doc_id: str):
    """
    Simulates loadting a document from storage
    """
    documents = {
        "doc1": """
        Microservices architecture improves scalability,
        allows independent deployment of services,
        enhances fault isolation, and supports faster development cycles.
        """
    }

    return documents.get(doc_id, "Document not found.")