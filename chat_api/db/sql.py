from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from chat_api.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_db():
    """Create database connection."""
    Base.metadata.create_all(bind=engine)


async def get_db_client() -> SessionLocal:
    """Return database client instance."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def drop_db():
    """Create database connection."""
    Base.metadata.drop_all(bind=engine)


async def close_db():
    """Close database connection."""
    pass
