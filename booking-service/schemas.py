from pydantic import BaseModel


class BookingBase(BaseModel):
    passenger_name: str
    flight_number: str
    seat_number: str
    status: str = "confirmee"


class BookingCreate(BookingBase):
    pass


class BookingOut(BookingBase):
    id: int

    class Config:
        from_attributes = True
