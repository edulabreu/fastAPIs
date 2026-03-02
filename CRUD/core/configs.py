from typing import List

from pydantic import AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings:
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:M225807@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings