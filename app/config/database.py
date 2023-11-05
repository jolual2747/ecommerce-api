from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base
from config import get_settings
from typing import Generator

settings = get_settings()

database_url = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@db:5432/{settings.DB_NAME}'
engine = create_engine(database_url, echo = True)

SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)
Base = declarative_base()

def get_db() -> Generator:   
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()