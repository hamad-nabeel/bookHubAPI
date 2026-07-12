from datetime import timedelta, datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.sql.functions import current_user

from .auth import get_current_user
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import SessionLocal
from passlib.context import CryptContext

from models import User, Book

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.close()
    finally:
        pass


user_dependency = Annotated[dict, Depends(get_current_user)]
db_dependency = Annotated[Session, Depends(get_db)]

class BookRequest(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str
    year: int = Field(gt=1900, lt=datetime.today().year)
    day: int = Field(gt=0, lt=32)
    month: int = Field(gt=0, lt=13)


@router.post("/books")
async def create_book(current_user: user_dependency, db: db_dependency, book_request: BookRequest):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    new_book = Book(
        title=book_request.title,
        description=book_request.description,
        year=book_request.year,
        day=book_request.day,
        month=book_request.month,
        author_id=current_user.get("id"),
    )
    db.add(new_book)
    db.commit()

@router.get("/all_books")
async def get_all_books(db: db_dependency, user: user_dependency):
    books = db.query(Book).filter(Book.author_id == user.get("id")).all()
    return books


@router.get("/{book_name}")
async def get_book(book_name: str, db: db_dependency, user: user_dependency):
    book = db.query(Book).filter(Book.title.ilike(book_name)).filter(Book.author_id==user.get('id')).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book



@router.get("/")
async def get_books(
        db: db_dependency, user: user_dependency, inputted_year: int, inputted_month: Optional[int] = None):
    query = db.query(Book).filter(
        Book.year == inputted_year,
        Book.author_id == user.get('id')
    )
    if inputted_month is not None:
        query = query.filter(Book.month == inputted_month)

    return query.all()


@router.put("/{book_id}")
async def update_book(book_id: int, book_request: BookRequest, db: db_dependency, user: user_dependency):
    book = db.query(Book).filter(Book.id == book_id).filter(Book.author_id==user.get('id')).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = book_request.title
    book.description = book_request.description
    book.year = book_request.year
    book.day = book_request.day
    book.month = book_request.month
    db.commit()
    return book

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: db_dependency, user: user_dependency):
    db.query(Book).filter(Book.id == book_id).filter(Book.author_id==user.get("id")).delete()
    db.commit()

