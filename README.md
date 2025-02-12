# notes-api
Backend для приложения с умными заметками

## Функционал
✅ Создание заметки
- Заголовок
- Описание
- Теги (можно несколько)
- Дата начала
- Дата завершения
✅ Редактирование/Удаление
- Можно менять текст, теги и даты
- Удалять ненужные заметки
✅ Поиск и фильтрация
- Поиск по заголовку/описанию
- Фильтр по тегам
- Фильтр по статусу (активные, завершённые)
✅ Уведомления на email
- За день до завершения — напоминание
- В день завершения — уведомление о просрочке
✅ Интеграция с Redis и RabbitMQ
- Redis: кэширование популярных запросов (например, последние 10 заметок)
- RabbitMQ: отправка фоновых задач на email-уведомления
✅ Авторизация (минимальная)

Регистрация/Login через email + пароль
JWT-токен для авторизованных запросов
Технологический стек
🛠 Backend: FastAPI + PostgreSQL + Redis + RabbitMQ
🖥 Frontend: Vue 3 (Composition API)
📦 Docker: для изоляции всех сервисов
☁ Деплой: сервер с Docker Compose (например, на VPS)

Расширения на будущее
- Возможность прикреплять файлы к заметкам
- Делать заметки публичными (для шеринга)
- Добавить тёмную тему
