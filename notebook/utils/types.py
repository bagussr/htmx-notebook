from typing import Optional
from typing_extensions import Annotated
from pydantic import AfterValidator, EmailStr, Field, SecretStr

from utils.password import password_hash


RequiredStr = Annotated[str, Field(..., min_length=1)]
RequiredEmail = Annotated[EmailStr, Field(..., min_length=1)]
PasswordStr = Annotated[SecretStr, AfterValidator(password_hash)]
OptionalStr = Annotated[Optional[str], Field(None)]
OptionalEmail = Annotated[Optional[EmailStr], Field(None)]
