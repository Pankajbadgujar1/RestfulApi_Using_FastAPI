from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:Pass@localhost/RESTapi_DB"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
print("Connection successfully creted")
Base = declarative_base()

print("Connection successfully creted")

print('Base : ',Base)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# run usgin cammand python -m app.seed