import sys
import os
import time
from datetime import datetime, timedelta

sys.path.append(os.path.join(os.getcwd(), "backend"))

print("Verifying TubeSage API Quota Optimization...")

try:
    from app.core.optimization.smart_cache import smart_cache
    from app.core.optimization.scheduler import batch_scheduler
    
    print("✅ Optimization modules loaded")
    
    # Test Smart Cache TTL
    # Viral score 1.0 -> 1 hour TTL
    ttl_viral = smart_cache.get_ttl(1.0)
    print(f"TTL for Viral (Score 1.0): {ttl_viral}s (Expected ~3600)")
    
    # Stagnant score 0.0 -> 7 days TTL
    ttl_stagnant = smart_cache.get_ttl(0.0)
    print(f"TTL for Stagnant (Score 0.0): {ttl_stagnant}s (Expected ~604800)")
    
    # Test Should Fetch
    res_id = "video_123"
    print(f"Should fetch new item? {smart_cache.should_fetch(res_id)}")
    
    smart_cache.update_entry(res_id, "data")
    print(f"Should fetch cached item (immediate)? {smart_cache.should_fetch(res_id)}")
    
    # Test Batch Scheduler
    items = [f"vid_{i}" for i in range(120)] # 120 items
    
    async def mock_fetch(chunk):
        return [f"processed_{x}" for x in chunk]
        
    import asyncio
    results = asyncio.run(batch_scheduler.execute_batch(items, mock_fetch))
    
    print(f"Batch processing count: {len(results)} (Expected 120)")
    
except Exception as e:
    print(f"❌ Verification failed: {e}")
    raise e
