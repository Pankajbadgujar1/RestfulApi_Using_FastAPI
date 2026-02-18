# 🚀 Scalable REST API with Authentication & Role-Based Access

This project is a full-stack assignment implementing a scalable REST API with JWT authentication, role-based access control, and a simple frontend UI for testing.

The backend is built using **FastAPI + PostgreSQL**, and the frontend is a lightweight **Vanilla JavaScript UI** for interacting with the APIs.

---

# 📌 Features

## 🔐 Authentication & Security
- User Registration with password hashing
- Login with JWT token generation
- Secure password storage using hashing
- Token-based authentication for protected routes
- Role-based access control (User / Admin)

## 👤 User Roles
- Normal users can manage their own tasks
- Admin users can:
  - View all registered users
  - Delete users

## 📝 Task Management (CRUD)
- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Tasks support title + description

## 📚 API Features
- RESTful design
- API versioning (`/api/v1`)
- Structured error handling
- Input validation
- Swagger API documentation

## 🖥️ Frontend UI
- Simple Vanilla JS UI
- Register & login users
- Store JWT in browser
- Create/update/delete tasks
- Admin panel for user management
- Clean styled interface

---

# 🏗️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- JWT (python-jose)
- Passlib (password hashing)
- Uvicorn

### Frontend
- HTML
- CSS
- Vanilla JavaScript

---

