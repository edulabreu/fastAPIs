from pydantic import BaseModel

class Curso(BaseModel):
    id: int
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo='Programação para leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algoritmos e Lógica de Programação', aulas=34, horas=66)
]