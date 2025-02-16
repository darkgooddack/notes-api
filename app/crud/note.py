from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse


# Создание заметки
async def create_note(db: AsyncSession, note: NoteCreate) -> NoteResponse:
    db_note = Note(
        title=note.title,
        description=note.description,
        created_date=note.created_date,
        deadline=note.deadline,
        user_id=note.user_id
    )
    db.add(db_note)
    await db.commit()  # Асинхронная коммитация
    await db.refresh(db_note)  # Асинхронное обновление, чтобы получить ID

    # Возвращаем NoteResponse, а не Note, чтобы соответствовать response_model
    return NoteResponse(
        id=db_note.id,
        title=db_note.title,
        description=db_note.description,
        user_id=db_note.user_id,
        created_date=db_note.created_date,
        deadline=db_note.deadline
    )



# Получение заметки по ID
async def get_note(db: AsyncSession, note_id: int):
    result = await db.execute(select(Note).filter(Note.id == note_id))
    return result.scalars().first()


# Получение всех заметок
async def get_notes(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Note).offset(skip).limit(limit))
    return result.scalars().all()


# Обновление заметки
async def update_note(db: AsyncSession, note_id: int, note_update: NoteUpdate):
    result = await db.execute(select(Note).filter(Note.id == note_id))
    db_note = result.scalars().first()
    if db_note:
        db_note.title = note_update.title
        db_note.content = note_update.content
        db_note.created_date = note_update.created_date
        db_note.deadline = note_update.deadline
        await db.commit()  # Асинхронная коммитация
        await db.refresh(db_note)  # Асинхронное обновление
        return db_note
    return None


# Удаление заметки
async def delete_note(db: AsyncSession, note_id: int):
    result = await db.execute(select(Note).filter(Note.id == note_id))
    db_note = result.scalars().first()
    if db_note:
        await db.delete(db_note)
        await db.commit()  # Асинхронная коммитация
        return db_note
    return None
