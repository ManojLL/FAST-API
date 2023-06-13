from pydantic import BaseModel, Field
from db.db import base


class User(BaseModel):
    user_email: str
    password: str
    qr_code: str
    user_name: str
