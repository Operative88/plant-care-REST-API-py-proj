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