from fastapi import FastAPI
from routes.user import userAPI

app = FastAPI()

app.include_router(userAPI)