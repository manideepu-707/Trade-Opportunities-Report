from fastapi import APIRouter

app=APIRouter()

@app.get('/')
def home():
    return "Welcome"