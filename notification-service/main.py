from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notification Service", version="1.0.0")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "notification-service"}


@app.get("/notifications", response_model=List[schemas.NotificationOut])
def list_notifications(db: Session = Depends(get_db)):
    return db.query(models.Notification).order_by(models.Notification.created_at.desc()).all()


@app.get("/notifications/flight/{flight_number}", response_model=List[schemas.NotificationOut])
def get_notifications_for_flight(flight_number: str, db: Session = Depends(get_db)):
    notifications = db.query(models.Notification).filter(
        models.Notification.flight_number == flight_number
    ).order_by(models.Notification.created_at.desc()).all()
    if not notifications:
        raise HTTPException(status_code=404, detail="Aucune notification pour ce vol")
    return notifications


@app.post("/notifications", response_model=schemas.NotificationOut, status_code=201)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    new_notification = models.Notification(**notification.model_dump())
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification
