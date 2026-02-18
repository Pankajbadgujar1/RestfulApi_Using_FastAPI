from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#  import DB objects (ONLY from database.py, do NOT recreate engine here)
from app.database import Base, engine

#  import models so tables get created
from app.models import user, task

#  import routers
from app.routes import auth
from app.routes import tasks

#import the admin routes
from app.routes import admin

# CREATE APP FIRST (must be before decorators)
app = FastAPI(title="REST API Assignment")


# Test DB connection on startup
@app.on_event("startup")
def test_connection():
    try:
        conn = engine.connect()
        print(" DB Connected Successfully")
        conn.close()
    except Exception as e:
        print(" DB Connection Failed:", e)


#  Create tables automatically
Base.metadata.create_all(bind=engine)


# CORS (needed if React frontend will call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers with prefix (better structure)
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])


app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


#  Root test route
@app.get("/")
def home():
    return {"message": "API is running successfully"}

