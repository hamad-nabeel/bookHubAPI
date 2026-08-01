# 📚 BookShelf API

BookShelf API is a RESTful backend built with **FastAPI** that allows users to create accounts, publish books, organize them into chapters, discover other authors, and save books to their personal library. The project was built to practice backend development with Python while following REST API principles, authentication, authorization, and database design.

---

## ✨ Features

- User registration and authentication
- JWT-based authentication
- User profiles
- Search users by username
- Create, read, update, and delete books
- Create, edit, and delete book chapters
- User ownership verification (users can only modify their own content)
- Save and unsave books from other users
- SQLite database with SQLAlchemy ORM
- Request validation with Pydantic
- Interactive API documentation with Swagger UI and ReDoc

---

## 🛠 Tech Stack

- **Backend:** FastAPI
- **Language:** Python
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Validation:** Pydantic
- **Server:** Uvicorn

---

## 📁 Project Structure

```
BookShelfApp/
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── books.py
│   └── chapters.py
│
├── models.py
├── database.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

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

**macOS / Linux**

```bash
source .fastapienv/bin/activate
```

**Windows**

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

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

**ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

## 🔑 Core Functionality

### Authentication

- Register a new account
- Log in using JWT authentication
- Secure authenticated endpoints

### Users

- View user profiles
- Search users by username

### Books

- Create books
- Retrieve books
- Update books
- Delete books

### Chapters

- Add chapters to books
- Edit chapters
- Delete chapters
- Organize books into multiple chapters

### Library

- Save books created by other users
- Remove books from saved collection
- View saved books

### Authorization

Ownership checks ensure users can only edit or delete the books and chapters they own.

---

## 🎯 Learning Goals

This project was built to strengthen understanding of:

- REST API design
- FastAPI routing
- Authentication and authorization
- SQLAlchemy ORM
- CRUD operations
- Database relationships
- Project organization using routers
- Backend best practices

---

## 🔮 Possible Future Improvements

While the project is feature complete, possible enhancements include:

- PostgreSQL support
- Alembic database migrations
- Docker support
- Unit and integration testing
- CI/CD pipeline
- Cloud deployment

---

## 📄 License

This project is open source and available for educational purposes.

