from sqlalchemy import Column, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from project_settings.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from City_app.models import DBCity


class DBTemperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    date_time = Column(Date)
    temperature = Column(Float)
    city = relationship(DBCity, back_populates="temperatures")

