from pydantic import BaseModel

class PlantBase(BaseModel):
    name: str
    location: str
    watering_frequency_days: int

class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: int

    class Config:
        orm_mode = True