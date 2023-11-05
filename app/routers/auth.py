from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserSignUp
from app.services.user import UserService
from app.config.database import get_db, SessionLocal
from app.auth.auth import create_access_token
from app.schemas.token import Token
from jose import jwt


auth_router = APIRouter(prefix='/auth')

@auth_router.post('/signUp', tags=['user'], response_model=dict)
async def sign_up(data:UserSignUp, db: SessionLocal = Depends(get_db)) -> dict:
    """Creates a new user."""
    UserService(db).signUp(data)
    return JSONResponse(status_code=201, content={"message":"User succesfully registered"})

@auth_router.post('/login', tags=['user'], response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)) -> Token:
    """Creates a new token by login."""
    user = UserService(db).authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= 'Could not validate user.')    
    token = create_access_token(username=user.username, id =user.id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(Token(access_token=token, token_type="bearer"))) 
