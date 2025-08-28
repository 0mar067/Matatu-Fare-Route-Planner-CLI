from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Create SQLite database engine
engine = create_engine('sqlite:///matatu.db', echo=False)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database by creating all tables"""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Get a new database session"""
    return SessionLocal()

def close_session(session):
    """Close the database session"""
    session.close()
