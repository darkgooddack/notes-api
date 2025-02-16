import logging
from datetime import date
from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.crud.note import create_note, get_note, get_notes, update_note, delete_note  # Переименовали функцию create_note
from app.core.database import get_db

router = APIRouter(prefix="/note")

@router.post(
    "/",
    response_model=NoteResponse,
    summary="Создание новой заметки",
    )
async def create(
    title: str = Form(...),
    description: str = Form(None),
    created_date: date = Form(...),
    deadline: date = Form(None),
    user_id: int = Form(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Создаёт новую заметку в базе данных.
    Если создание прошло успешно, возвращает информацию о созданной заметке.
    В случае ошибки, будет выведено сообщение об ошибке.
    """

    note_data = NoteCreate(
        title=title,
        description=description,
        created_date=created_date,
        deadline=deadline,
        user_id=user_id
    )

    try:
        note = await create_note(db=db, note=note_data)
        logging.info("✅ Заметка успешно добавлена в БД")
        return note  # NoteResponse будет автоматически сериализован

    except Exception as e:
        logging.error(f"❌ При создании заметки произошла ошибка: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"При создании заметки произошла ошибка: {str(e)}",
        )


@router.get(
    "/{note_id}",
    response_model=NoteResponse,
    summary="Получение информации о конкретной заметке по её ID",
)
async def get_one(
        note_id: int,
        db: AsyncSession = Depends(get_db)
):
    """
    Получение данных о конкретной заметке по её уникальному идентификатору.

    Этот эндпоинт позволяет получить все данные заметки по её ID. Если заметка с таким
    ID существует в базе данных, возвращаются её данные: название, описание, дата
    создания и срок действия. Если заметка с указанным ID не найдена, возвращается ошибка 404.

    **Пример успешного ответа:**
    ```json
    {
        "id": 1,
        "title": "Заметка 1",
        "description": "Описание заметки",
        "user_id": 1,
        "created_date": "2025-02-16",
        "deadline": "2025-02-20"
    }
    ```
    """

    try:
        note = await get_note(db=db, note_id=note_id)

        if not note:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Заметка с ID {note_id} не найдена."
            )

        logging.info(f"✅ Заметка с ID {note_id} найдена в БД")
        return note

    except Exception as e:
        logging.error(f"❌ Ошибка при получении заметки с ID {note_id}: {str(e)}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Заметка с ID {note_id} не найдена в БД"
        )


@router.get(
    "/",
    response_model=List[NoteResponse],
    summary="Получение списка заметок с пагинацией",
)
async def get_all(
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
):
    """
    Этот эндпоинт позволяет получить список всех заметок в базе данных.
    Поддерживается пагинация, позволяющая управлять количеством возвращаемых записей.

    Параметры:
    - `skip`: Количество записей, которые нужно пропустить (по умолчанию 0).
    - `limit`: Максимальное количество заметок, которые будут возвращены в ответе (по умолчанию 100).

    Возвращает:
    - Список заметок с их ID, названием, описанием, датой создания и сроком действия.
    """
    try:
        notes = await get_notes(db=db, skip=skip, limit=limit)
        logging.info(f"✅ Заметки найдены в БД")
        if not notes:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Заметки не найдены."
            )
        return notes

    except Exception as e:
        logging.error(f"❌ Ошибка при получении списка заметок: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Произошла ошибка при обработке запроса."
        )


@router.put("/{note_id}", response_model=NoteResponse)
async def update(
    note_id: int,
    note_update: NoteUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Этот эндпоинт обновляет заметку по её ID.
    Изменяются только те поля, которые были переданы в запросе.
    """
    try:
        # Извлекаем существующую заметку по её ID
        note = await get_note(db=db, note_id=note_id)

        if not note:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Заметка с ID {note_id} не найдена."
            )

        # Обновление только тех полей, которые были переданы
        if note_update.title is not None:
            note.title = note_update.title
        if note_update.description is not None:
            note.description = note_update.description
        if note_update.deadline is not None:
            note.deadline = note_update.deadline

        # Сохраняем изменения в базе данных
        db.add(note)  # Добавляем заметку в сессию
        await db.commit()  # Коммитим изменения
        await db.refresh(note)  # Обновляем объект из БД

        logging.info(f"✅ Заметка с ID {note_id} успешно обновлена")
        return note

    except Exception as e:
        logging.error(f"❌ Ошибка при обновлении заметки с ID {note_id}: {str(e)}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Произошла ошибка при обработке запроса."
        )



@router.delete("/{note_id}", response_model=NoteResponse)
async def delete(note_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_note(db=db, note_id=note_id)
