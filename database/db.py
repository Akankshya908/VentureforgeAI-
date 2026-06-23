from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    """SQLAlchemy declarative base."""


# Default database: SQLite (local) for scaffold compatibility.
DATABASE_URL: str = "sqlite:///./ventureforge_ai.db"

# SQLAlchemy engine & session factory.
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)

