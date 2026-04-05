from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

#tabela w bazie danych
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Funkcja pomocnicza do dostępu do bazy
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/plants", response_model=schemas.Plant)
def create_plant(plant: schemas.PlantCreate, db: Session = Depends(get_db)):
    db_plant = models.PlantModel(**plant.dict())
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant

@app.get("/plants", response_model=list[schemas.Plant])
def get_plants(db: Session = Depends(get_db)):
    return db.query(models.PlantModel).all()

@app.delete("/plants/{plant_id}")
def delete_plant(plant_id: int, db: Session = Depends(get_db)):
    db_plant = db.query(models.PlantModel).filter(models.PlantModel.id == plant_id).first()
    if db_plant is None:
        raise HTTPException(status_code=404, detail="Nie znaleziono rośliny o podanym ID")
    
    db.delete(db_plant)
    db.commit()
    return {"message": f"Roślina o ID {plant_id} została usunięta"}