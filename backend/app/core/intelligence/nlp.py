import spacy
from typing import List, Dict

class NLPProcessor:
    def __init__(self, model_name: str = "en_core_web_sm"):
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            # Fallback or instruction to download
            # In production, ensure the model is downloaded during build
            print(f"Warning: Model {model_name} not found. Please run 'python -m spacy download {model_name}'")
            self.nlp = None

    def process_text(self, text: str) -> Dict:
        if not self.nlp or not text:
            return {"entities": [], "keywords": [], "sentiment_score": 0.0}

        doc = self.nlp(text)
        
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        
        # Simple keyword extraction (nouns and proper nouns)
        keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
        
        # Basic sentiment placeholder (Spacy doesn't have built-in sentiment without extensions)
        # We'll use a simple polarity check or upgrade to TextBlob/VADER if needed later.
        # For now, just return 0.0 or integrate a sentiment library.
        sentiment_score = 0.0 

        return {
            "entities": entities,
            "keywords": list(set(keywords)),
            "sentiment_score": sentiment_score
        }

nlp_processor = NLPProcessor()
