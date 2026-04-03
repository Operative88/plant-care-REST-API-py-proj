from fastapi import FastAPI

#instancja aplikacji

api = FastAPI(
    title="plantcare API",
    description="API do zarządzania domowymi roślinami",
    version="0.1.0"
)

TEMP_DATABASE = [
    {"id": 1, "name": "monstera dziurawa", "location": "salon", "watering_frequency_data": 7},
    {"id": 2, "name": "skrzydłokwiat", "location": "sypialnia", "watering_frequency_days": 4}
]
