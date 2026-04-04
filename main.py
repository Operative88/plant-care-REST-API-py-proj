from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#instancja aplikacji
app = FastAPI(title="PlantCare API")

class Plant(BaseModel):
    id: int
    name: str
    location: str
    watering_frequency_days: int

TEMP_DATABASE: list[Plant] = []

@app.get("/plants", response_model=list[Plant])
def get_all_plants():
    return TEMP_DATABASE

@app.post("/plants", response_model=Plant)
def create_plant(plant: Plant):
    if any(p.id == plant.id for p in TEMP_DATABASE):
        raise HTTPException(status_code=400, detail="Roślina o danym id już istnieje")
    
    TEMP_DATABASE.append(plant)
    return plant

@app.get("/plants/{plant_id}", response_model=Plant)
def get_plant(plant_id: int):
    for plant in TEMP_DATABASE:
        if plant.id == plant_id: return plant
        
        raise HTTPException(status_code=404, detail="Nie znaleziono rośliny o podanym id")

        