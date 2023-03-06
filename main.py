from fastapi import FastAPI
from typing import List
from uuid import uuid4
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.female,
        roles=[Role.user, Role.admin]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;