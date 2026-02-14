from datetime import datetime, timedelta
from typing import Optional, Dict, Any

class SmartCache:
    def __init__(self):
        # In-memory mock for Redis. In production, use self.redis.set(key, val, ex=ttl)
        self._cache: Dict[str, Dict] = {}
        
    def get_ttl(self, volatility_score: float) -> int:
        """
        Calculates TTL based on content volatility.
        Score 0.0 (Stagnant) -> 7 days
        Score 1.0 (Viral) -> 1 hour
        """
        # Linear interpolation or custom curve
        min_ttl = 3600      # 1 hour
        max_ttl = 604800    # 7 days
        
        # Invert score: High volatility = Low TTL
        factor = 1.0 - max(0.0, min(1.0, volatility_score))
        
        return int(min_ttl + (max_ttl - min_ttl) * factor)

    def should_fetch(self, resource_id: str, volatility_score: float = 0.5) -> bool:
        """
        Determines if we should fetch fresh data or use cache.
        """
        if resource_id not in self._cache:
            return True
            
        entry = self._cache[resource_id]
        ttl = self.get_ttl(volatility_score)
        
        age = (datetime.utcnow() - entry["last_updated"]).total_seconds()
        return age > ttl

    def update_entry(self, resource_id: str, data: Any = None):
        """
        Updates the cache entry timestamp.
        """
        self._cache[resource_id] = {
            "last_updated": datetime.utcnow(),
            "data": data
        }

smart_cache = SmartCache()
