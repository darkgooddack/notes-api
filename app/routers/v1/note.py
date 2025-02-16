from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.schemas.note import NoteCreate, NoteUpdate, Note
from app.crud.note import create_note as create_note_in_db, get_note, update_note, delete_note  # Переименовали функцию create_note
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=Note)
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_db)):
    return await create_note_in_db(db=db, note=note)  # Используем новое имя функции

@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: int, db: AsyncSession = Depends(get_db)):
    return await get_note(db=db, note_id=note_id)

@router.get("/", response_model=List[Note])
async def get_notes(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_notes(db=db, skip=skip, limit=limit)

@router.put("/{note_id}", response_model=Note)
async def update_note(note_id: int, note_update: NoteUpdate, db: AsyncSession = Depends(get_db)):
    return await update_note(db=db, note_id=note_id, note_update=note_update)

@router.delete("/{note_id}", response_model=Note)
async def delete_note(note_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_note(db=db, note_id=note_id)
