from sqlalchemy import Column,Integer,String
from db.db import base


class UserModel(base):
    __tablename__ = "sec_user"

    USER_ID = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(45),index=True)
    user_email = Column(String(45), unique=True,index=True)
    qr_code = Column(String(45), unique=True,index=True)
    password = Column(String(45))
