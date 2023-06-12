from pydantic import BaseModel


class User(BaseModel):
    user_email: str
    password: str
    qr_code: str
    user_name: str

    class Config:
        orm_model= True
