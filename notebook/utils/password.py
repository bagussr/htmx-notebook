from bcrypt import hashpw, checkpw, gensalt
from pydantic import SecretStr


def password_hash(password: SecretStr) -> SecretStr:
    return SecretStr(hashpw(password.get_secret_value().encode(), gensalt()).decode())


def verify_password(password: str, hashed_password: str) -> bool:
    return checkpw(password.encode(), hashed_password.encode())
