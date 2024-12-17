from app.core.models.base import Base
from sqlalchemy.orm import Mapped


class Rooms(Base):
    __tablename__ = "rooms"

    room_number: Mapped[int]
    room_type: Mapped[str]
    price: Mapped[float]
    status: Mapped[str]
