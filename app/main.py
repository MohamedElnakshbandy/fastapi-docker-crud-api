from fastapi import FastAPI

from app import database, models
from app.routers import items, system, auth

# Create database tables


app = FastAPI()

app.include_router(system.router)
app.include_router(items.router)
app.include_router(auth.router)