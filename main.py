from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

#tabela w bazie danych
models.Base.metadata.create_all