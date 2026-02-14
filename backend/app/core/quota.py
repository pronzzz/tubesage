import redis.asyncio as redis
from .config import get_settings
from datetime import datetime, timedelta

settings = get_settings()

class APIQuotaMonitor:
    def __init__(self):
        self.redis = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
        self.QUOTA_LIMIT = 10000  # Daily quota limit
        self.QUOTA_KEY = f"youtube_quota:{datetime.utcnow().strftime('%Y-%m-%d')}"

    async def check_quota(self, cost: int = 1) -> bool:
        """
        Check if we have enough quota to perform the action.
        """
        current_usage = await self.redis.get(self.QUOTA_KEY)
        if current_usage and int(current_usage) + cost > self.QUOTA_LIMIT:
            return False
        return True

    async def consume_quota(self, cost: int = 1):
        """
        Increment the quota usage.
        """
        await self.redis.incrby(self.QUOTA_KEY, cost)
        # Set expiry for 24 hours to clean up old keys
        await self.redis.expire(self.QUOTA_KEY, 86400)

    async def get_usage(self) -> int:
        val = await self.redis.get(self.QUOTA_KEY)
        return int(val) if val else 0

quota_monitor = APIQuotaMonitor()
