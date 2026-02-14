from .nlp import nlp_processor
from .embeddings import embedding_engine
from typing import Dict, Any

class ContentAnalyzer:
    def analyze_video_content(self, title: str, description: str) -> Dict[str, Any]:
        """
        Orchestrates the analysis of video content.
        """
        # NLP Processing
        title_nlp = nlp_processor.process_text(title)
        desc_nlp = nlp_processor.process_text(description)
        
        # Embeddings
        title_emb = embedding_engine.generate_embedding(title)
        desc_emb = embedding_engine.generate_embedding(description)
        
        # Combine results
        # For MVP, we use title keywords as "topics". 
        # Future: Use clustering on embeddings to find topic clusters.
        topics = title_nlp.get("keywords", []) + desc_nlp.get("keywords", [])
        
        return {
            "title_analysis": title_nlp,
            "description_analysis": desc_nlp,
            "title_embedding": title_emb,
            "description_embedding": desc_emb,
            "topics": list(set(topics)),
            "sentiment_score": (title_nlp.get("sentiment_score", 0) + desc_nlp.get("sentiment_score", 0)) / 2
        }

analyzer = ContentAnalyzer()
