from fastapi import APIRouter
from CRUD.api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/escola', tags=["escola"])
