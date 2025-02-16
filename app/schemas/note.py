from pydantic import BaseModel
from datetime import date
from typing import Optional

# Схема для создания заметки
class NoteCreate(BaseModel):
    title: str
    description: Optional[str] = None  # Используем description, чтобы соответствовать полю в базе
    user_id: int
    created_date: date
    deadline: date

# Схема для обновления заметки
class NoteUpdate(BaseModel):
    title: str
    description: Optional[str] = None  # Исправляем content на description
    created_date: date
    deadline: date

# Схема для ответа
class NoteResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    user_id: int
    created_date: date
    deadline: date

    class Config:
        from_attributes = True
