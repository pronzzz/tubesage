from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from .core.config import get_settings
from .models import Base
from .database import get_db
from .core.quota import quota_monitor

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        # Check DB connection
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"
        
    # Check Redis/Quota
    try:
        quota_usage = await quota_monitor.get_usage()
        redis_status = "connected"
    except Exception as e:
        redis_status = f"disconnected: {str(e)}"
        quota_usage = -1

    return {
        "status": "ok", 
        "project": settings.PROJECT_NAME,
        "database": db_status,
        "redis": redis_status,
        "quota_usage": quota_usage
    }

@app.get("/")
async def root():
    return {"message": "Welcome to TubeSage API"}

from pydantic import BaseModel
class VideoAnalysisRequest(BaseModel):
    title: str
    description: str

@app.post("/api/v1/analyze/content")
async def analyze_content(request: VideoAnalysisRequest):
    from .core.intelligence.analyzer import analyzer
    
    results = analyzer.analyze_video_content(request.title, request.description)
    
    # Return a subset for the API response, but full data would be saved to DB in a real flow
    return {
        "topics": results["topics"],
        "sentiment": results["sentiment_score"],
        "embedding_preview": results["title_embedding"][:5] if results["title_embedding"] else []
    }

@app.get("/api/v1/trends/analyze/{video_id}")
async def analyze_trend(video_id: str):
    from .core.trends.detector import trend_detector
    # In a real scenario, we would fetch MetricTimeSeries from DB for this video_id
    # Mocking time series data (timestamp, views)
    import time
    now = time.time()
    # Simulate an accelerating series: 100 -> 110 -> 130 -> 160 -> 200
    mock_series = [
        (now - 4000, 100),
        (now - 3000, 110),
        (now - 2000, 130),
        (now - 1000, 160),
        (now, 200)
    ]
    
    signal, confidence = trend_detector.detect_trend(mock_series)
    
    return {
        "video_id": video_id,
        "signal": signal,
        "confidence": confidence,
        "data_points": len(mock_series)
    }

class SimulationRequest(BaseModel):
    channel_id: str
    current_avg_views: int
    upload_frequency_multiplier: float = 1.0
    quality_multiplier: float = 1.0

@app.post("/api/v1/predictions/simulate")
async def simulate_strategy(request: SimulationRequest):
    from .core.predictions.simulator import strategy_simulator
    
    current_stats = {"avg_views": request.current_avg_views}
    changes = {
        "upload_frequency_multiplier": request.upload_frequency_multiplier,
        "quality_multiplier": request.quality_multiplier
    }
    
    result = strategy_simulator.simulate_scenario(current_stats, changes)
    return result

class CompetitorAnalysisRequest(BaseModel):
    target_channel_topics: List[str]
    competitor_topics: List[str]

@app.post("/api/v1/competitors/analyze")
async def analyze_competitors(request: CompetitorAnalysisRequest):
    from .core.competitors.overlap import overlap_analyzer
    from .core.competitors.gap_detector import gap_detector
    
    overlap_score = overlap_analyzer.calculate_overlap(request.target_channel_topics, request.competitor_topics)
    gaps = gap_detector.find_gaps(request.target_channel_topics, request.competitor_topics)
    
    return {
        "overlap_score": round(overlap_score, 2),
        "content_gaps": gaps,
        "gap_count": len(gaps)
    }

@app.get("/api/v1/optimization/quota-stats")
async def get_quota_stats():
    from .core.quota import quota_monitor
    from .core.optimization.smart_cache import smart_cache
    
    current_usage = await quota_monitor.get_usage()
    
    # Mocking savings calculation for demo
    # In reality, we'd track "requests_saved" in Redis
    estimated_savings = int(current_usage * 0.4) 
    
    return {
        "current_daily_usage": current_usage,
        "limit": quota_monitor.QUOTA_LIMIT,
        "remaining": quota_monitor.QUOTA_LIMIT - current_usage,
        "smart_cache_entries": len(smart_cache._cache),
        "estimated_requests_saved": estimated_savings,
        "status": "Healthy" if current_usage < quota_monitor.QUOTA_LIMIT * 0.9 else "Critical"
    }

@app.get("/api/v1/recommendations/{channel_id}")
async def get_recommendations(channel_id: str):
    from .core.recommendations.engine import recommendation_engine
    return recommendation_engine.generate_recommendations(channel_id)


