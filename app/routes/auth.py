from fastapi import APIRouter, HTTPException,  Depends
from app.database import get_db
from app.schemas.user import UserCreate,LoginSchema
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.utils.security import hash_password, verify_password
from app.models.user import User
from app.core.jwt_handler import create_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    #  check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
        )

    # hash password
    hashed = hash_password(user.password)

    user_data = user.dict()
    user_data["password"] = hashed

    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_token({
    "sub": str(user.id),   # MUST be string
    "role": user.role
    })
    return {
        "access_token": token,
        "token_type": "bearer"
    }

def admin_required(current_user=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
