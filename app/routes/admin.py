from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.dependencies import admin_required

router = APIRouter()


#  ADMIN: get all users
@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
):
    return db.query(User).all()


# ADMIN: delete any user
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(admin_required)
    ):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}
