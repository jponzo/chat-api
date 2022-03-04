from motor.motor_asyncio import AsyncIOMotorClient
from chat_api.core.config import settings

DB_URL = settings.DB_URL

db_client: AsyncIOMotorClient = None


async def get_db_client() -> AsyncIOMotorClient:
    """Return database client instance."""
    db_client = AsyncIOMotorClient(DB_URL)
    return db_client


async def initialize_db():
    """Create database connection."""
    db_client = AsyncIOMotorClient(DB_URL)
    db = db_client.users
    col = db.users
    await col.create_index("email", unique=True)


async def close_db():
    """Close database connection."""
    db_client.close()
