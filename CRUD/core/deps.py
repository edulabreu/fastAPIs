from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.core.database import Session  # ou o nome que você usou

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        try:
            yield session
        finally:
            await session.close()