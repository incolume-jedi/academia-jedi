"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

import os
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

load_dotenv(Path(__file__).parent.joinpath('.env'))

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
print(SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

db = {
    'admin': {
        'username': 'admin',
        'full_name': 'Admin User',
        'email': 'admin@example.com',
        #  admin
        'hashed_password': '$2b$12$yICb/THawlTcEyircA0udOw1Zgdwpd0wSoPL1VHUA8UUE93yTciU6',
        'disabled': False,
    },
    'user1': {
        'username': 'user1',
        'full_name': 'User One',
        'email': 'user1@example.com',
        #  user1
        'hashed_password': '$2b$12$WWrEuKNdrj49wz1kVGN8Fu2.HbpVodUlL2BqPzcHuNvjjo0StTzLe',
        'disabled': True,
    },
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = ''


class User(BaseModel):
    username: str
    email: str = ''
    full_name: str = ''
    disabled: bool = False


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(db, username=token_data.username)
    if not user:
        raise credential_exception

    return user


async def get_current_active_user(
    current_user: UserInDB = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Inactive user',
        )

    return current_user


@app.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username},
        expires_delta=access_token_expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get('/users/me/', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get('/users/me/items')
async def read_own_items(
    current_user: User = Depends(get_current_active_user),
):
    return [
        {
            'items': [
                {'item_id': 1, 'description': 'item 1'},
                {'item_id': 2, 'description': 'item 2'},
                {'item_id': 3, 'description': 'item 3'},
            ],
            'owner': User(**current_user.__dict__),
        },
    ]


if __name__ == '__main__':  # pragma: no cover
    print(get_password_hash('user1'))
