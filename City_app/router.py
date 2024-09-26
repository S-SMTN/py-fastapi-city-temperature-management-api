from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List

from project_settings.custom_exceptions.http_exceptions import CityNotFoundException
from project_settings.dependecies import get_db
from . import schemas, crud

city_router = APIRouter()


@city_router.post(
    path="/cities",
    response_model=schemas.City,
    status_code=status.HTTP_201_CREATED
)
async def create_city(
    city_data: schemas.CityCreate,
    db: AsyncSession = Depends(get_db)
) -> schemas.City:
    return await crud.create_city(
        db=db,
        city_data=city_data
    )


@city_router.get(
    path="/cities",
    response_model=List[schemas.City],
    status_code=status.HTTP_200_OK
)
async def get_cities(db: AsyncSession = Depends(get_db)) -> List[schemas.City]:
    return await crud.get_all_cities_with_temperatures(db=db)


@city_router.get(
    path="/cities/{city_id}",
    response_model=schemas.City,
    status_code=status.HTTP_200_OK
)
async def retrieve_city(
    city_id: int,
    db: AsyncSession = Depends(get_db)
) -> schemas.City:
    city = await crud.get_city(db=db, city_id=city_id)

    if city is None:
        raise CityNotFoundException(city_id)
    return city


@city_router.put(
    path="/cities/{city_id}/",
    response_model=schemas.City,
    status_code=status.HTTP_200_OK
)
async def update_city(
    city_id: int,
    city_data: schemas.CityCreate,
    db: AsyncSession = Depends(get_db)
) -> schemas.City:
    updated_city = await crud.update_city(
        db=db,
        city_id=city_id,
        city_data=city_data
    )

    if updated_city is None:
        raise CityNotFoundException(city_id)

    return updated_city


@city_router.delete(
    path="/cities/{city_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_city(
    city_id: int,
    db: AsyncSession = Depends(get_db)
) -> None:
    city = await crud.delete_city(db=db, city_id=city_id)

    if city is None:
        raise CityNotFoundException(city_id)
