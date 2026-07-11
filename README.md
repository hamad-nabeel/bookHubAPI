# 📚 BookShelf API

BookShelf API is a RESTful backend built with **FastAPI** that allows users to create accounts and publish their own books. The project is designed as a learning exercise to practice backend development, authentication, database design, and REST API principles using Python.

## Features

### Current

* User registration and authentication
* JWT-based authentication
* Create, read, update, and delete books
* User ownership verification (users can only modify their own books)
* SQLite database with SQLAlchemy ORM
* Automatic interactive API documentation with Swagger UI

### Planned

* User profiles
* Book chapters
* Comments and reviews
* Likes and favorites
* Search by title or author
* Admin role and moderation
* Reading lists
* Follow authors
* Pagination and filtering

## Tech Stack

* **Backend:** FastAPI
* **Language:** Python
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **Validation:** Pydantic
* **Server:** Uvicorn

## Project Structure

```text
BookShelfApp/
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   └── books.py
│
├── models.py
├── database.py
├── main.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd BookShelfApp
```

### 2. Create a virtual environment

```bash
python -m venv .fastapienv
```

### 3. Activate the virtual environment

macOS/Linux

```bash
source .fastapienv/bin/activate
```

Windows

```bash
.fastapienv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

## Learning Goals

This project is intended to strengthen understanding of:

* REST API design
* FastAPI routing
* SQLAlchemy relationships
* Authentication and authorization
* CRUD operations
* Database design
* Project organization using routers
* Backend best practices

## Future Improvements

* Switch from SQLite to PostgreSQL
* Database migrations using Alembic
* Docker support
* Unit and integration testing
* CI/CD pipeline
* Cloud deployment

## License

This project is open source and available for educational purposes.
