from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from Temperature_app.models import DBTemperature


class TemperaturesGetter:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db
        self.stmt = (
        select(DBTemperature)
        .options(selectinload(DBTemperature.city))
        .order_by(DBTemperature.date_time)
    )

    async def get_result(self) -> List[DBTemperature]:
        temperatures = await self.db.scalars(self.stmt)
        return list(temperatures)


async def get_all_temperatures(db: AsyncSession) -> List[DBTemperature]:
    temperatures_getter = TemperaturesGetter(db=db)
    return await temperatures_getter.get_result()


async def get_temperature_by_city_id(
    db: AsyncSession,
    city_id: int
) -> List[DBTemperature]:
    temperatures_getter = TemperaturesGetter(db=db)
    temperatures_getter.stmt = (
        temperatures_getter.stmt
        .where(DBTemperature.city_id == city_id)
    )
    return await temperatures_getter.get_result()
