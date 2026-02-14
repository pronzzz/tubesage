import sys
import os
import asyncio

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage Recommendation Engine...")

try:
    from app.core.recommendations.engine import recommendation_engine, Recommendation
    
    print("✅ Recommendation module loaded")
    
    channel_id = "test_channel"
    recs = recommendation_engine.generate_recommendations(channel_id)
    
    print(f"Generated {len(recs)} recommendations")
    
    if len(recs) > 0:
        first = recs[0]
        print(f"Top Recommendation: [{first.category}] {first.suggestion} (Impact: {first.impact_score})")
        
        # Verify sorting
        if recs[0].impact_score < recs[-1].impact_score:
            raise Exception("Recommendations not sorted by impact score!")
            
    print("✅ Logic verification passed")

except Exception as e:
    print(f"❌ Verification failed: {e}")
    raise e
