from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    role: Role
