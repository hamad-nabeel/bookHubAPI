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
    hashed_password = Column(String)
    role = Column(String)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("user.id"))
    year = Column(Integer)
    day = Column(Integer)
    month = Column(Integer)
    description = Column(String)









