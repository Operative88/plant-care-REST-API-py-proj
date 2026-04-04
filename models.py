from sqlalchemy import Column, Integer, String
from .database import Base

class PlantModel(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    watering_frequency_days = Column(Integer)
    