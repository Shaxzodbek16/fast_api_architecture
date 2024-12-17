from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.core.models.base import Base


class Bookings(Base):
    __tablename__ = 'bookings'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'), primary_key=True)
    check_in: Mapped[datetime]
    check_out: Mapped[datetime]
    total_price: Mapped[float]
    status: Mapped[str]
