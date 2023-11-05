from pydantic import BaseModel

class UserSignUp(BaseModel):
    email:str
    username:str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "email": "admin@admin.com",
                    "username": "admin",
                    "password": "admin"
                }
            ]
        }
    }

class UserLogin(BaseModel):
    email:str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "email": "admin@admin.com",
                    "password": "admin"
                }
            ]
        }
    }
