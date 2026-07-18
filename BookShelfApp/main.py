import models
from database import engine
from fastapi import FastAPI
from routers import auth, books, user
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)

app.include_router(user.router)