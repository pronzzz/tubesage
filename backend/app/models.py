from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Channel(Base):
    __tablename__ = "channels"

    id = Column(String, primary_key=True, index=True)  # YouTube Channel ID
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    custom_url = Column(String, unique=True, nullable=True)
    published_at = Column(DateTime)
    thumbnail_url = Column(String, nullable=True)
    country = Column(String, nullable=True)
    
    # Current snapshot metrics
    subscriber_count = Column(Integer, default=0)
    video_count = Column(Integer, default=0)
    view_count = Column(Integer, default=0)
    
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    videos = relationship("Video", back_populates="channel")
    metrics = relationship("MetricTimeSeries", back_populates="channel")

class Video(Base):
    __tablename__ = "videos"

    id = Column(String, primary_key=True, index=True)  # Video ID
    channel_id = Column(String, ForeignKey("channels.id"))
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    published_at = Column(DateTime, index=True)
    thumbnail_url = Column(String, nullable=True)
    tags = Column(JSON, nullable=True)
    category_id = Column(String, nullable=True)
    duration = Column(String, nullable=True)  # ISO 8601 duration
    
    # Analysis Data
    title_embedding = Column(JSON, nullable=True) # Vector stored as JSON list
    description_embedding = Column(JSON, nullable=True)
    sentiment_score = Column(Float, nullable=True)
    topics = Column(JSON, nullable=True) # List of extracted topics
    
    # Snapshot metrics
    view_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    
    channel = relationship("Channel", back_populates="videos")
    metrics = relationship("MetricTimeSeries", back_populates="video")

class MetricTimeSeries(Base):
    __tablename__ = "metric_time_series"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Polymorphic checks or separate logic could be used, but simple nullable FKs work for now
    channel_id = Column(String, ForeignKey("channels.id"), nullable=True)
    video_id = Column(String, ForeignKey("videos.id"), nullable=True)
    
    # Metrics
    views = Column(Integer, nullable=True)
    subscribers = Column(Integer, nullable=True)
    likes = Column(Integer, nullable=True)
    comments = Column(Integer, nullable=True)
    
    channel = relationship("Channel", back_populates="metrics")
    video = relationship("Video", back_populates="metrics")

class TrendSignal(Base):
    __tablename__ = "trend_signals"

    id = Column(Integer, primary_key=True, index=True)
    entity_id = Column(String, index=True) # Video ID or Topic ID
    signal_type = Column(String, index=True) # Emerging, Trending, etc.
    confidence_score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

