from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from .config import get_settings
import os

settings = get_settings()

class YouTubeClient:
    def __init__(self):
        self.api_key = settings.YOUTUBE_API_KEY
        self.youtube = self._build_service()

    def _build_service(self):
        # Uses API Key for public data. OAuth2 will be integrated for user-specific actions later.
        return build("youtube", "v3", developerKey=self.api_key)

    async def get_channel_details(self, channel_id: str):
        request = self.youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=channel_id
        )
        response = request.execute()
        return response

    async def search_videos(self, query: str, max_results: int = 10):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results,
            type="video"
        )
        response = request.execute()
        return response

# Singleton instance
youtube_client = YouTubeClient()
