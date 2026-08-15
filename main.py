from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Flights Service", version="1.0.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "flights-service"}


@app.get("/flights", response_model=List[schemas.FlightOut])
def list_flights(
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.Flight)
    if search:
        query = query.filter(
            or_(
                models.Flight.flight_number.ilike(f"%{search}%"),
                models.Flight.destination.ilike(f"%{search}%"),
            )
        )
    return query.all()


@app.get("/flights/{flight_id}", response_model=schemas.FlightOut)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = db.query(models.Flight).filter(models.Flight.id == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Vol introuvable")
    return flight


@app.post("/flights", response_model=schemas.FlightOut, status_code=201)
def create_flight(flight: schemas.FlightCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Flight).filter(
        models.Flight.flight_number == flight.flight_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Ce numéro de vol existe déjà")

    new_flight = models.Flight(**flight.model_dump())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight


@app.put("/flights/{flight_id}", response_model=schemas.FlightOut)
def update_flight(flight_id: int, flight: schemas.FlightUpdate, db: Session = Depends(get_db)):
    db_flight = db.query(models.Flight).filter(models.Flight.id == flight_id).first()
    if not db_flight:
        raise HTTPException(status_code=404, detail="Vol introuvable")

    for key, value in flight.model_dump(exclude_unset=True).items():
        setattr(db_flight, key, value)

    db.commit()
    db.refresh(db_flight)
    return db_flight


@app.delete("/flights/{flight_id}", status_code=204)
def delete_flight(flight_id: int, db: Session = Depends(get_db)):
    db_flight = db.query(models.Flight).filter(models.Flight.id == flight_id).first()
    if not db_flight:
        raise HTTPException(status_code=404, detail="Vol introuvable")

    db.delete(db_flight)
    db.commit()
    return None
