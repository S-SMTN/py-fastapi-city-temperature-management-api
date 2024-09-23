from typing import List

from pydantic import BaseModel, Field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Temperature_app.schemas import TemperatureCreate, Temperature


class CityBase(BaseModel):
    name: str = Field(max_length=176)
    additional_info: str


class CityCreate(CityBase):
    temperatures: List[TemperatureCreate] = []


class City(CityBase):
    temperatures: List[Temperature] = []

    class Config:
        orm_mode = True
