from pydantic import BaseModel

class PlantBase(BaseModel):
    name: str
    location: str
    watering_frequency_days: int
    last_watered = str
class PlantCreate(PlantBase):
    pass

class Plant(PlantBase):
    id: int

    class Config:
        orm_mode = True