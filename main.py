from fastapi import FastAPI

from typing import Optional, Any

from time import sleep

from fastapi import Depends #Injeção de Dependencias - db: Any = Depends(fake_db) -
from fastapi import Response
from fastapi import Path
from fastapi import Header
from fastapi import HTTPException
from fastapi import status

from Intro.models import Curso, cursos


def fake_db():
    try:
        print('Abrindo conexão com o Banco de Dados')
        sleep(1)
    finally:
        print('Fechando conexão com o Banco de Dados')
        sleep(1)

app = FastAPI(title='Swagger API´s X')

@app.get('/cursos', status_code=status.HTTP_200_OK)
async def get_cursos( db: Any = Depends(fake_db) ):
    return cursos

@app.get('/cursos/{curso_id}', status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int = Path(title='ID do Curso', description='Deve ser um inteiro'),db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}', status_code=status.HTTP_200_OK)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id informado - curso {curso_id}')

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um curso com o id informado - curso {curso_id}')

@app.get('/calculadora') #Query Parameter and Header
async def calcular(a: Optional[int]=0,b: Optional[int]=0,c: Optional[int]=0, apikey = Header(), db: Any = Depends(fake_db)):
    soma = a + b + c
    return f'resultado: {soma} {apikey}'


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)