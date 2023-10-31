from app.schemas.product import Product
from app.models.user import User
from app.schemas.user import UserSignUp

# user_su = UserSignUp(email='admin@admin.com', username='admin', password='admin')
# print(user_su)
# user_su_dict = user_su.model_dump()
# password = user_su_dict.pop('password')
# user = User(**user_su_dict)
# user.hash_password(password=password)
# print(user.__dict__)

from app.config.database import SessionLocal

db = SessionLocal()
results = db.query(User).filter(User.username == 'admin').first()
print(results.hash_password())