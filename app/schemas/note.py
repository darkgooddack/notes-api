from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     created_at = Column(DateTime, server_default=func.now())


# Схема для создания заметки
class NoteCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int
    created_date: datetime
    deadline: Optional[datetime] = None

# Схема для обновления заметки
class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    created_date: Optional[datetime] = None
    deadline: Optional[datetime] = None

# Схема для отображения заметки
class Note(BaseModel):
    id: int
    title: str
    content: str
    created_date: datetime
    deadline: datetime

    class Config:
        from_attributes = True
