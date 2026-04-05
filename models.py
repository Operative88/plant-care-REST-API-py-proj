from sqlalchemy import Column, Integer, String
from .database import Base
from datetime import date

#wygląd tabeli w sql
class PlantModel(Base):
    __tablename__ = "plants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    watering_frequency_days = Column(String)
    last_watered = Column(Date, nullable=True, default=date.today)