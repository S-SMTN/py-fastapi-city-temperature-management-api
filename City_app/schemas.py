from typing import List, Optional

from pydantic import BaseModel, field_validator
from City_app.schema_validators.validators import StrLengthValidator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Temperature_app.schemas import TemperatureCreate, Temperature


class CityBase(BaseModel):
    name: str
    additional_info: str

    @classmethod
    @field_validator("name")
    def name_length(cls, name: str) -> str:
        StrLengthValidator.validate("City name", name, 176)

        return name


class CityCreate(CityBase):
    temperatures: Optional[List[TemperatureCreate]] = []


class City(CityBase):
    temperatures: Optional[List[Temperature]] = []

    class Config:
        orm_mode = True
