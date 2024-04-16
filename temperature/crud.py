from datetime import datetime

from sqlalchemy.orm import Session

from city import models as city_models
from temperature.utils import get_temperature
from temperature import models


async def update_temperature_for_all_cities(db: Session):
    cities = db.query(city_models.DBCity).all()
    temperatures = []

    for city in cities:
        city_name = city.name
        db_temperature = models.DBTemperature(
            city_id=city.id,
            date_time=datetime.now(),
            temperature=await get_temperature(city_name),
        )
        db.add(db_temperature)
        db.commit()
        db.refresh(db_temperature)
        temperatures.append(db_temperature)

    return temperatures


def get_all_temperature_records(db: Session):
    return db.query(models.DBTemperature).all()


def get_temperature_by_city_id(db: Session, city_id: int):
    return db.query(models.DBTemperature).filter(
        models.DBTemperature.city_id == city_id
    )
