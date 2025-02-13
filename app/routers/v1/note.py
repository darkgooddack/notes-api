from fastapi import APIRouter
from app.schemas.note import NoteCreate,NoteUpdate,Note   # Импортируйте схемы, если они у вас есть
from app.crud.note import create_note, get_note, update_note, delete_note  # Импортируйте функции CRUD

router = APIRouter()

@router.post("/")
def create(note: NoteCreate):
    return create_note(note)

@router.get("/{note_id}")
def read(note_id: int):
    return get_note(note_id)

@router.put("/{note_id}")
def update(note_id: int, note: NoteUpdate):
    return update_note(note_id, note)

@router.delete("/{note_id}")
def delete(note_id: int):
    return delete_note(note_id)

