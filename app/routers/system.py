from fastapi import APIRouter
from sqlalchemy import text

from app import database

router = APIRouter(
    tags=["System"]
)


@router.get("/")
def home():
    return {"message": "Hello from FastAPI inside Docker!"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/db-check")
def db_check():
    with database.engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        return {
            "database": "connected",
            "version": result.scalar()
        }