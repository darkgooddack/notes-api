from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate

# Создание заметки
def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        title=note.title,
        content=note.content,
        start_date=note.start_date,
        end_date=note.end_date,
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Получение заметки по ID
def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

# Получение всех заметок
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()

# Обновление заметки
def update_note(db: Session, note_id: int, note_update: NoteUpdate):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.title = note_update.title
        db_note.content = note_update.content
        db_note.start_date = note_update.start_date
        db_note.end_date = note_update.end_date
        db.commit()
        db.refresh(db_note)
        return db_note
    return None

# Удаление заметки
def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
        return db_note
    return None
