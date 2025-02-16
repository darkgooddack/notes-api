from datetime import date  # Импортируем только дату

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

from app.models.user import User


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_date = Column(Date, default=date.today)  # Передаем функцию без скобок
    deadline = Column(Date, default=date.today)  # Тоже без скобок

    user = relationship("User", back_populates="notes")
