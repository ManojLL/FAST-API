from sqlalchemy import Column,Integer,String
from db.db import base


class User(base):
    __tablename__ = "sec_user"
    user_id = Column(Integer, primary_key=True),
    user_name = Column(String(45)),
    user_email = Column(String(45), unique=True),
    qr_code = Column(String(45), unique=True),
    password = Column(String(45))
