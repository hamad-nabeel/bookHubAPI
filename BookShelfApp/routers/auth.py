from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
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
    password: str
    role: str = Field(default="user")

@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: db_dependency):
    new_user=User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=bcrypt_context.hash(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


