from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from project_settings.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Temperature_app.models import DBTemperature


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String())
    additional_info = Column(String(176))
    temperatures = relationship(DBTemperature, back_populates="city")
