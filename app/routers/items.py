from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, database, schemas

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.post("/")
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(database.get_db)
):
    return crud.create_item(db, item)


@router.get("/")
def get_items(
    db: Session = Depends(database.get_db)
):
    return crud.get_items(db)


@router.get("/{item_id}")
def get_item(
    item_id: int,
    db: Session = Depends(database.get_db)
):
    item = crud.get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.put("/{item_id}")
def update_item(
    item_id: int,
    updated_item: schemas.ItemCreate,
    db: Session = Depends(database.get_db)
):
    item = crud.update_item(db, item_id, updated_item)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(database.get_db)
):
    item = crud.delete_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item deleted successfully"}