from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from CRUD.core.configs import settings

engine = create_async_engine(settings.DB_URL, echo=False)

Session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)
