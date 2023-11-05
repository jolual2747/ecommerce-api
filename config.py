from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_NAME:str
    PGADMIN_DEFAULT_EMAIL:str
    PGADMIN_DEFAULT_PASSWORD:str
    SECRET_KEY:str
    ALGORITHM:str
    TEST_USER:str
    TEST_PASSWORD:str
    class Config:
        env_file:str = '.env'

@lru_cache
def get_settings():
    return Settings()