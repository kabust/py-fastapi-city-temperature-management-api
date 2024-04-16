from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from temperature import schemas, crud
from dependencies import get_db

router = APIRouter()


@router.post("/temperatures/update/", response_model=list[schemas.Temperature])
async def fetch_temperature_for_all_cities(db: Session = Depends(get_db)):
    return await crud.update_temperature_for_all_cities(db)


@router.get("/temperatures/", response_model=list[schemas.Temperature])
def read_temperature_records(
        city_id: int | None = None,
        db: Session = Depends(get_db)
):
    if city_id:
        return crud.get_temperature_by_city_id(db, city_id)

    return crud.get_all_temperature_records(db)
