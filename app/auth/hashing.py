from passlib.context import CryptContext

class Hashing():
    def __init__(self):
        self.bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
    
    def hash_password(self, password:str):
        hashed_password = self.bcrypt_context.hash(password)
        return hashed_password

    def verify_password(self, password:str, hashed_password:str):
        return self.bcrypt_context.verify(password, hashed_password)