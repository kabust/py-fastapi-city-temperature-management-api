from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from city import schemas, crud
from dependencies import get_db

router = APIRouter()


@router.get("/cities/", response_model=list[schemas.City])
def read_all_cities(db: Session = Depends(get_db)):
    return crud.get_all_cities(db)


@router.get("/cities/{city_id}/", response_model=schemas.City)
def read_city(city_id: int, db: Session = Depends(get_db)):
    city = crud.get_city_by_id(db, city_id)

    if city is None:
        raise HTTPException(
            status_code=404,
            detail="City with this ID does not exists"
        )

    return city


@router.post("/cities/", response_model=schemas.City)
def create_city(
        city: schemas.CityCreate,
        db: Session = Depends(get_db)
):
    db_city = crud.get_city_by_name(db, city.name)

    if db_city:
        raise HTTPException(
            status_code=400,
            detail="City with this name already exists"
        )

    return crud.create_city(db, city)


@router.put("/cities/{city_id}/", response_model=schemas.City)
def update_city(
        new_info: schemas.CityCreate,
        city_id: int,
        db: Session = Depends(get_db)
):
    db_city = crud.get_city_by_id(db, city_id)

    if db_city is None:
        raise HTTPException(
            status_code=404,
            detail="City with this ID does not exists"
        )

    return crud.update_city_by_id(db, new_info, city_id)


@router.delete("/cities/{city_id}/", response_model=schemas.City)
def remove_city(city_id: int, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_id(db, city_id)

    if db_city is None:
        raise HTTPException(
            status_code=404,
            detail="City with this ID does not exists"
        )

    return crud.delete_city_by_id(db, city_id)
