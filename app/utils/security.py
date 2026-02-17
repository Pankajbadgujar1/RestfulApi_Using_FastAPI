from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ truncate to bcrypt limit (72 bytes)
def _truncate(password: str) -> str:
    return password.encode("utf-8")[:72].decode("utf-8", "ignore")

def hash_password(password: str) -> str:
    password = _truncate(password)
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    password = _truncate(password)
    return pwd_context.verify(password, hashed_password)
