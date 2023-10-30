from app.schemas.user import UserSignUp
from app.models.user import User

class UserService:
    def __init__(self, db):
        self.db = db

    def signUp(self, user: UserSignUp):
        user_to_add = User(email = user.email, username = user.username)
        user_to_add.hashed_password(user.password)
        self.db.add(user_to_add)


