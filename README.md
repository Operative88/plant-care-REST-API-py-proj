#  PlantCare API

A modern REST API built with **Python** and **FastAPI** to help you manage your home jungle. Track your plants, their locations, and never forget about watering again.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-05998b)
![SQLite](https://img.shields.io/badge/database-SQLite-003b57)

---

##  Features

- **Full CRUD:** Create, Read, Update, and Delete plants in your collection.
- **Persistent Storage:** Data is stored in a local SQLite database using SQLAlchemy ORM.
- **Data Validation:** Robust input validation powered by Pydantic schemas.
- **Auto-generated Docs:** Interactive Swagger UI documentation available out-of-the-box.
- **Watering Tracker:** Dedicated endpoint to update the last watering date.

---

##  Tech Stack

* **Language:** Python
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Database:** SQLite
* **Validation:** [Pydantic](https://docs.pydantic.dev/)

---

##  Getting Started

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository
```bash
git clone [https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/plantcare-api.git](https://github.com/TWOJA-NAZWA-UZYTKOWNIKA/plantcare-api.git)
cd plantcare-api
```

### 2. Create a virtual environment
Windows:
```bash   
python -m venv venv
venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn main:app --reload
```

## API Usage & Documentation
Once the server is running, you can access the interacive documentation at:
http://127.0.0.1:8000/docs

Key Endpoints:
• GET /plants - List all plants.

• POST /plants - Add a new plant (Validates input data).

• GET /plants/{id} - Get details of a specific plant.

• POST /plants/{id}/water - Update the watering timestamp for a plant.

• DELETE /plants/{id} - Remove a plant from the database.