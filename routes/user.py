from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from models import user
from schemas.models import User
from models.user import UserModel
from sqlalchemy.orm import Session
from db.db import engine, sessionLocal

userAPI = APIRouter()

user.base.metadata.create_all(bind=engine)

def get_db():
    try:
        databse = sessionLocal()
        yield databse
    finally:
        databse.close()



@userAPI.get("/users")
async def getAllUsers(db:Session = Depends(get_db)):
    return db.query(UserModel).all()



@userAPI.get("/users/{userId}")
async def getAllUsersById(userId: int, db:Session = Depends(get_db)):
    getUser =  db.query(UserModel).filter(UserModel.USER_ID == userId).first()

    if getUser is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {userId} : Does not exist"
        )

    return getUser


@userAPI.post("/users")
async def createUser(add_user: User, db:Session = Depends(get_db)):
    new_user = UserModel()
    new_user.user_email = add_user.user_email
    new_user.user_name = add_user.user_name
    new_user.qr_code = add_user.qr_code
    new_user.password = add_user.password

    db.add(new_user)
    db.commit()
    return add_user
