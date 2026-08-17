from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Booking Service", version="1.0.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "booking-service"}


@app.get("/bookings", response_model=List[schemas.BookingOut])
def list_bookings(db: Session = Depends(get_db)):
    return db.query(models.Booking).all()


@app.get("/bookings/{booking_id}", response_model=schemas.BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Réservation introuvable")
    return booking


@app.post("/bookings", response_model=schemas.BookingOut, status_code=201)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    new_booking = models.Booking(**booking.model_dump())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


@app.delete("/bookings/{booking_id}", response_model=schemas.BookingOut)
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Réservation introuvable")

    booking.status = "annulee"
    db.commit()
    db.refresh(booking)
    return booking
