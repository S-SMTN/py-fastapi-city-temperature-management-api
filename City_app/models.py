from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from project_settings.database import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String())
    additional_info = Column(String(176))
    temperatures = relationship(
        argument="DBTemperature",
        back_populates="city",
    )
