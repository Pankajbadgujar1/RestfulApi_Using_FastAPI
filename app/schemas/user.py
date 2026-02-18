from pydantic import BaseModel, EmailStr , Field

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    role: str | None = "user"

class LoginSchema(BaseModel):
    email: EmailStr
    password: str