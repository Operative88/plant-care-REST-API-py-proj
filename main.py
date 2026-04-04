from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

#instancja aplikacji
app = FastAPI(title="PlantCare API")

class Plant(BaseModel):
    id: int
    name: str
    location: str
    watering_frequency_days: int

TEMP_DATABASE: List[Plant] = []

@app.get("/plants", response_model=List[Plant])
def get_all_plants():
    return TEMP_DATABASE

@app.post("/plants", response_model=Plant)
def create_plant(plant: Plant):
    #sprawdzenie czy roślina o tym id już istnieje
    if any(p.id == plant.id for p in TEMP_DATABASE):
        raise HTTPException(status_code=400, detail="Roślina o tym ID już istnieje")
    
    TEMP_DATABASE.append(plant)
    return plant