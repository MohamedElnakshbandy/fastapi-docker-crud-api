from fastapi import FastAPI

from app import database, models
from app.routers import items, system

# Create database tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(system.router)
app.include_router(items.router)