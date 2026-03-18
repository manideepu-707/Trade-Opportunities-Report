from fastapi import FastAPI
from routes.auth_route import router as auth_router
from routes.analyze import router
from routes.home import app as home
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Trade Opportunities API")

app.include_router(home)
app.include_router(auth_router)
app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)