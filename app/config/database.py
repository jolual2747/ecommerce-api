from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base
from typing import Generator
import urllib
import os

host_server = os.environ.get('HOST_SERVER', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('DB_SERVER_PORT', '5432')))
database_name = os.environ.get('DB_NAME', 'fastapi')
db_username = urllib.parse.quote_plus(str(os.environ.get('DB_USERNAME', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('DB_PASSWORD', 'secret')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('SSL_MODE','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
engine = create_engine(DATABASE_URL, echo = True)
print(DATABASE_URL)
print(DATABASE_URL)
print(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)
Base = declarative_base()

def get_db() -> Generator: 
    """Get a database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()