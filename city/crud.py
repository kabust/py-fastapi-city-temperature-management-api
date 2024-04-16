from sqlalchemy.orm import Session

import models, schemas


def get_all_cities(db: Session):
    return db.query(models.DBCity).all()


def get_city_by_id(db: Session, city_id: int):
    return (
        db.query(models.DBCity).
        filter(models.DBCity.id == city_id).
        first()
    )


def update_city_by_id(db: Session, city: schemas.CityCreate, city_id: int):
    db_city = (
        db.query(models.DBCity).
        filter(models.DBCity.id == city_id).
        first()
    )
    db_city.name = city.name
    db_city.additional_info = city.additional_info

    db.commit()
    db.refresh(db_city)

    return db_city


def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.DBCity(
        name=city.name,
        additional_info=city.additional_info
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)

    return db_city


def delete_city_by_id(db: Session, city_id: int):
    db_city = (
        db.query(models.DBCity).
        filter(models.DBCity.id == city_id).
        first()
    )
    db.delete(db_city)
    db.commit()

    return db_city
