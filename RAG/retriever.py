import faiss
from sentence_transformers import SentenceTransformer
from documents import DOCUMENTS

class EmbeddingRetriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.embeddings = self.model.encode(DOCUMENTS)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def retrieve(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)

        return [DOCUMENTS[i] for i in indices[0]]
