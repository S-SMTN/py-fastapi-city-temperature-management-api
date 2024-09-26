from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from project_settings.dependecies import get_db
from . import schemas, crud

temperature_router = APIRouter()


@temperature_router.get(
    path="/temperatures",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.Temperature]
)
async def get_temperatures(
    db: AsyncSession = Depends(get_db)
) -> List[schemas.Temperature]:
    return await crud.get_all_temperatures(db=db)
