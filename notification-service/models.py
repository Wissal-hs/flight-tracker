from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True, nullable=False)
    message = Column(String, nullable=False)
    type = Column(String, default="info")  # info, retard, annulation
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
