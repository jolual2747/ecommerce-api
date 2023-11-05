from datetime import timedelta, datetime
from fastapi import Depends, HTTPException
from starlette import status
from app.schemas.token import Token, TokenData
import os
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/login')

def create_access_token(username: str, id: int, expires_mins:int = 20):
    """Creates access token with expiration"""
    encode = {'sub': username, 'id': id}
    expires = datetime.utcnow() + timedelta(minutes=expires_mins)
    encode.update({'exp':expires})
    return jwt.encode(encode, key = os.environ.get("SECRET_KEY"), algorithm=os.environ.get("ALGORITHM"))

async def get_current_user(token:Token = Depends(oauth2_bearer)):
    """Gets current user and validates token."""
    try:
        payload = jwt.decode(token, key=os.environ.get("SECRET_KEY"), algorithms = [os.environ.get("ALGORITHM")])
        username: str = payload.get('sub')
        id: int = payload.get('id')
        if username is None or id is None:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Could not validate user." )
        return TokenData(username=username, id=id)
    except JWTError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Could not validate user.')
