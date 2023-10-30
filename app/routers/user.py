from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.schemas.user import UserSignUp
from app.services.user import UserService
from app.config.database import get_db, SessionLocal

login_router = APIRouter()

@login_router.post('/signUp', tags=['user'], response_model=dict)
def sign_up(data:UserSignUp, db: SessionLocal = Depends(get_db)) -> dict:
    UserService(db).signUp(data)
    return JSONResponse(status_code=201, content={"message":"User succesfully registered"})
