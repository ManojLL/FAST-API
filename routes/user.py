from fastapi import APIRouter
from schemas.models import User
from models.user import User
from sqlalchemy.orm import Session
from db.db import engine, sessionLocal, base
user = APIRouter()


# @user.get("/users")
# async def getAllUsers():
#     return connection.execute(users.select()).fetchall()

#
# @user.get("/users/{userId}")
# async def getAllUsersById(userId: int):
#     return connection.execute(users.select().where(users.c.id == userId)).fetchall()
#

@user.post("/users")
async def createUser(user: User):

