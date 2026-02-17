from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Pass@localhost/RESTapi_DB"

try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("Database connected successfully!")
    conn.close()
except Exception as e:
    print("Database connection failed")
    print(e)
