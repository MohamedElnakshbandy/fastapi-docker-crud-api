from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password

def get_items(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    new_item = models.Item(
        name=item.name,
        description=item.description
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def update_item(db: Session, item_id: int, updated_item: schemas.ItemCreate):
    item = get_item(db, item_id)

    if item is None:
        return None

    item.name = updated_item.name
    item.description = updated_item.description

    db.commit()
    db.refresh(item)

    return item


def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)

    if item is None:
        return None

    db.delete(item)
    db.commit()
    return item

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed = hash_password(user.password)

    new_user = models.User(
        email=user.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user