from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from alembic import context
from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.note import *
from app.models.user import *

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL_asyncpg)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# Function to run migrations in 'offline' mode
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url", settings.DATABASE_URL_asyncpg)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Function to run migrations in 'online' mode
async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

    # Создаём асинхронную сессию
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with engine.begin() as connection:
        # Применяем миграции
        await connection.run_sync(Base.metadata.create_all)
        await connection.commit()

# Выполняем миграции в зависимости от режима (офлайн/онлайн)
if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio
    asyncio.run(run_migrations_online())
