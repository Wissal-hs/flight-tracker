from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class FlightBase(BaseModel):
    flight_number: str
    destination: str
    origin: str
    departure_time: datetime
    status: str = "a_l_heure"
    gate: Optional[str] = None


class FlightCreate(FlightBase):
    pass


class FlightUpdate(BaseModel):
    destination: Optional[str] = None
    origin: Optional[str] = None
    departure_time: Optional[datetime] = None
    status: Optional[str] = None
    gate: Optional[str] = None


class FlightOut(FlightBase):
    id: int

    class Config:
        from_attributes = True
