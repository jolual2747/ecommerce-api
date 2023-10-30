import bcrypt
import jwt

class Hashing():
    def __init__(self) -> None:
        pass
    
    def hash_password(self, password:str):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

    def verify_password(self, password:str, hashed_password:str):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    

hash = Hashing()
pwd = "gabe2747"

hashed = Hashing.hash_password(pwd)
print(hashed)
print(hash.verify_password(pwd, hashed))