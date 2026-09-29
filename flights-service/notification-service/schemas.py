from pydantic import BaseModel
from datetime import datetime


class NotificationBase(BaseModel):
    flight_number: str
    message: str
    type: str = "info"


class NotificationCreate(NotificationBase):
    pass


class NotificationOut(NotificationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
