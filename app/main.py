import json
import logging
from pathlib import Path

import redis
from config import Config, load_config
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

GET_PATH = Path(__file__).resolve().parent.parent
ENV_PATH = GET_PATH / '.env'
config: Config = load_config(path=str(ENV_PATH))

logger = logging.getLogger(name = __name__)
logging.basicConfig(format = config.log.format,
                    level = config.log.level,)

logger.info('Logging started.')

data = redis.Redis(host=config.db.host, port=config.db.port, db=0, decode_responses=True)
try:
    data.ping()
    logger.info('Подключение с Redis установлено.')
except redis.ConnectionError:
    logger.error('Не удалось подключиться к Redis.')

class Film(BaseModel):
    title: str
    is_seen: bool = False
    rating: int | None = None

app = FastAPI()

@app.exception_handler(redis.ConnectionError)
def redis_exception_handler(request: Request, exc: redis.ConnectionError):
    logger.error(f"Глобальный перехват: Redis недоступен. Ошибка: {exc}")
    return JSONResponse(
        status_code=503,
        content={"detail": "Сервис временно недоступен: отсутствует подключение к базе данных фильмов."},
    )

@app.get('/')
def root():
    return {'message': 'Это API-кинотека, для просмотра'
            'вашего каталога перейдите на ~/catalog\n'
            'Полную документацию можно найти на ~/docs'}

@app.get('/catalog/')
def get_catalog():
    keys = data.keys('film:*')
    catalog = []
    for key in keys:
        film_raw = data.get(key)
        if film_raw:
            catalog.append(json.loads(film_raw))
    return {'catalog': catalog}

@app.post('/')
def add_film(film: Film):
    data.set(f'film:{film.title}', film.model_dump_json())
    return {'message': 'Фильм успешно добавлен.', 'film': film.model_dump()}

@app.get('/catalog/{title}')
def get_film(title: str):
    film_raw = data.get(f'film:{title}')

    if film_raw is not None:
        return {'message': "Фильм найден.", 'data': json.loads(film_raw)}
    raise HTTPException(
        status_code=404,
        detail='Фильм не найден.'
    )

@app.delete('/catalog/del/{title}')
def del_film(title: str):
    result = data.delete(f'film:{title}')
    if result == 1:
        return {'message': f'Фильм {title} успешно удален.'}

    raise HTTPException(
        status_code=404,
        detail='Фильм не найден.'
    )