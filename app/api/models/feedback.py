from sqlalchemy import ForeignKey

from app.core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Feedback(Base):
    __tablename__ = "feedback"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    comment: Mapped[str]
