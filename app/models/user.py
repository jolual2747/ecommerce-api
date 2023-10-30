from app.config.database import Base
from sqlalchemy import Column, String, Integer
import bcrypt

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String)
    hashed_password = Column(String)

    def hash_password(self, password:str):
        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.hashed_password = hash.decode('utf-8')
        
    def verify_password(self, password:str, hashed_password:str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))