from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingEngine:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        # This will download the model on first use
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str) -> List[float]:
        if not text:
            return []
        
        embedding = self.model.encode(text)
        # Convert numpy array to list for JSON serialization
        return embedding.tolist()

embedding_engine = EmbeddingEngine()
