from app.schemas.user import UserSignUp
from app.models.user import User
from app.auth.hashing import Hashing
from datetime import timedelta, datetime
from config import get_settings
from jose import jwt

class UserService:
    def __init__(self, db):
        self.db = db
        self._Hashing = Hashing()
        self._settings = get_settings()

    def signUp(self, user: UserSignUp):
        """Creates new users."""
        user_to_add = User(email = user.email, username = user.username, hashed_password = self._Hashing.hash_password(user.password))
        self.db.add(user_to_add)
        self.db.commit()

    def authenticate_user(self, username, password):
        """Login a user."""
        user = self.db.query(User).filter(User.username == username).first()       
        if not user:
            return False
        if not self._Hashing.verify_password(password, user.hashed_password):
            return False
        return user