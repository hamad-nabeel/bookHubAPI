from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    biography = Column(String)
    hashed_password = Column(String)
    role = Column(String)
    number_of_books = Column(Integer)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("user.id"))
    year = Column(Integer)
    day = Column(Integer)
    month = Column(Integer)
    description = Column(String)
    author = relationship("User", back_populates="books")

class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    book_id = Column(Integer, ForeignKey("book.id"))
    author_id = Column(Integer, ForeignKey("user.id"))
    text = Column(String)











