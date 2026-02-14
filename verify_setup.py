import sys
import os

# Add backend to sys.path
sys.path.append(os.path.join(os.getcwd(), "backend"))

# Mock environment variables for Pydantic
os.environ["YOUTUBE_API_KEY"] = "dummy_key"
os.environ["POSTGRES_USER"] = "postgres"
os.environ["POSTGRES_PASSWORD"] = "password"
os.environ["POSTGRES_DB"] = "tubesage"
os.environ["DATABASE_URL"] = "postgresql+asyncpg://postgres:password@localhost:5432/tubesage"

print("Verifying TubeSage Backend Setup...")

try:
    from app.core.config import get_settings
    print("✅ Config loaded")
except ImportError as e:
    print(f"❌ Config import failed: {e}")

try:
    from app.models import Channel, Video, MetricTimeSeries
    print("✅ Models loaded")
except ImportError as e:
    print(f"❌ Models import failed: {e}")

try:
    from app.core.youtube_client import youtube_client
    print("✅ YouTube Client loaded")
except ImportError as e:
    print(f"❌ YouTube Client import failed: {e}")

try:
    from app.database import get_db
    print("✅ Database module loaded")
except ImportError as e:
    print(f"❌ Database module import failed: {e}")

print("\nSetup verification complete (syntax check only).")
print("Note: Runtime dependencies (Postgres/Redis) require Docker.")
