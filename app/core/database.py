from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Создаём движок SQLAlchemy для асинхронного взаимодействия с БД
engine = create_async_engine(settings.DATABASE_URL_asyncpg, future=True, echo=True)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
