from pydantic import BaseModel, PastDate


class TemperatureBase(BaseModel):
    city_id: int
    date_time: PastDate
    temperature: float


class TemperatureCreate(TemperatureBase):
    pass


class Temperature(TemperatureBase):
    id: int

    class Config:
        orm_mode = True
