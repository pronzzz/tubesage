import sys
import os

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage Intelligence Engine...")

try:
    import spacy
    print(f"✅ Spacy installed: {spacy.__version__}")
except ImportError:
    print("❌ Spacy not found")

try:
    import sentence_transformers
    print(f"✅ Sentence Transformers installed: {sentence_transformers.__version__}")
except ImportError:
    print("❌ Sentence Transformers not found")

try:
    from app.core.intelligence.analyzer import analyzer
    print("✅ Analyzer module loaded")
except Exception as e:
    print(f"❌ Analyzer module failed to load: {e}")

print("\nNote: Runtime requires actual models to be downloaded.")
