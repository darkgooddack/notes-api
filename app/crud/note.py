from sqlalchemy.orm import Session
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate

# id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     created_date = Column(DateTime, server_default=func.now())
#     deadline = Column(DateTime)

# Создание заметки
def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        title=note.title,
        content=note.content,
        created_date=note.created_date,
        deadline=note.deadline,
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
        db_note.created_date = note_update.created_date
        db_note.deadline = note_update.deadline
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
