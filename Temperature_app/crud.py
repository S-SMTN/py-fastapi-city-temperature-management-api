from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from Temperature_app.models import DBTemperature


async def get_all_temperatures(db: AsyncSession) -> List[DBTemperature]:
    stmt = (
        select(DBTemperature)
        .options(selectinload(DBTemperature.city))
        .order_by(DBTemperature.date_time)
    )
    temperatures = await db.scalars(stmt)
    return list(temperatures)
