from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True, nullable=False)
    destination = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    status = Column(String, default="a_l_heure")  # a_l_heure, retarde, annule
    gate = Column(String, nullable=True)
