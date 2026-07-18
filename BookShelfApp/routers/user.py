from datetime import timedelta, datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.sql.functions import user

from models import User
from .auth import get_current_user
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import SessionLocal

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class EditBiography(BaseModel):
    biography: Optional[str]


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]

def produce_my_profile(user: User):
    lines = []
    lines.append("Name: " + user.first_name + " " + user.last_name + "\n")
    lines.append("Username: " + user.username + "\n")
    lines.append("Email: " + user.email + "\n")
    lines.append("Biography: " + user.biography + "\n")
    lines.append("Number of books: " + str(user.number_of_books) + "\n")
    return PlainTextResponse("\n".join(lines), media_type="text/plain")

def produce_searched_profile(user: User):
    lines = []
    lines.append("Name: " + user.first_name + " " + user.last_name + "\n")
    lines.append("Username: " + user.username + "\n")
    lines.append("Biography: " + user.biography + "\n")
    lines.append("Number of books: " + str(user.number_of_books) + "\n")
    lines.append("Books Published: " + "\n")
    for book in user.books:
        lines.append(book.title + "\n")
    return PlainTextResponse("\n".join(lines), media_type="text/plain")
@router.put("/biography")
async def edit_biography(bio: EditBiography, db: db_dependency, user: user_dependency):
    current_user = db.query(User).filter(user.get("id") == User.id).first()
    if not current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    current_user.biography = bio.biography
    db.commit()


@router.get("/me/profile")
async def get_my_profile(user: user_dependency, db: db_dependency):
    current_user: Optional[User] =  db.query(User).filter(user.get("id") == User.id).first()
    if not current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return produce_my_profile(current_user)

@router.get("/{username}/profile")
async def get_profile(username: str, db: db_dependency):
    searched_user: Optional[User] = db.query(User).filter(User.username.ilike(username)).first()
    if not searched_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return produce_searched_profile(searched_user)


