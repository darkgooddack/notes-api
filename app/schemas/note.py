from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Схема для создания заметки
class NoteCreate(BaseModel):
    title: str
    content: str
    start_date: datetime
    end_date: datetime

# Схема для обновления заметки
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

# Схема для отображения заметки
class Note(BaseModel):
    id: int
    title: str
    content: str
    start_date: datetime
    end_date: datetime

    class Config:
        from_attributes = True
