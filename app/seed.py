from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password


def seed_admin():

    db: Session = SessionLocal()

    # Check if admin already exists
    existing_admin = db.query(User).filter(User.email == "admin@mail.com").first()

    if existing_admin:
        print("Admin already exists")
        db.close()
        return

    # Create admin user
    admin = User(
        username="admin",
        email="admin@mail.com",
        password=hash_password("admin123"),
        role="admin"
    )

    db.add(admin)
    db.commit()
    db.close()

    print("Admin user seeded successfully")


if __name__ == "__main__":
    seed_admin()
