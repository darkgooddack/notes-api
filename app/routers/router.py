from fastapi import APIRouter
from .v1.note import router as note_router  # Импортируйте свой router для /notes

v1 = APIRouter()

# Включение других роутеров
v1.include_router(note_router, tags=["Заметки"])
