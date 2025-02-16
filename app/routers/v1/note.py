from datetime import date
from typing import List

from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.crud.note import create_note, get_note, get_notes, update_note, delete_note  # Переименовали функцию create_note
from app.core.database import get_db

router = APIRouter(prefix="/note")

@router.post("/", response_model=NoteResponse)
async def create(
    title: str = Form(...),
    description: str = Form(None),
    created_date: date = Form(...),
    deadline: date = Form(None),
    user_id: int = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # Создаём объект через форму
    note_data = NoteCreate(
        title=title,
        description=description,
        created_date=created_date,
        deadline=deadline,
        user_id=user_id
    )

    # Создаём заметку в базе данных
    return await create_note(db=db, note=note_data)

@router.get("/{note_id}", response_model=NoteResponse)
async def get_one(note_id: int, db: AsyncSession = Depends(get_db)):
    return await get_note(db=db, note_id=note_id)

@router.get("/", response_model=List[NoteResponse])
async def get_all(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_notes(db=db, skip=skip, limit=limit)

@router.put("/{note_id}", response_model=NoteResponse)
async def update(note_id: int, note_update: NoteUpdate, db: AsyncSession = Depends(get_db)):
    return await update_note(db=db, note_id=note_id, note_update=note_update)

@router.delete("/{note_id}", response_model=NoteResponse)
async def delete(note_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_note(db=db, note_id=note_id)
