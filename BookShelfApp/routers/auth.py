from datetime import timedelta, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import SessionLocal
from passlib.context import CryptContext

from models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)



## JWT Encoding details
SECRET_KEY = "7cd802e77c631ee8bec50293b1f29acb3ad8fa967f514334ffe8b74e7d6eb90c" ##generated using openssl rand -hex 32
ALGORITHM = "HS256"

##---------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db_dependency = Annotated[Session, Depends(get_db)]

class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    role: str = Field(default="user")


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_token(username: str,user_id: str, expire_delta: timedelta):
    encode={
        "sub": username,
        "id": user_id,
    }
    expires = datetime.utcnow() + expire_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: db_dependency):
    new_user=User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=bcrypt_context.hash(user.password),
        username=user.username,
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/token', status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = create_token(user.username, user.id, timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}





