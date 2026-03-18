from fastapi import APIRouter
from core.auth import create_access_token


router = APIRouter()

# Dummy login (no DB required as per task)
@router.post("/login")
def login(username: str):
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}