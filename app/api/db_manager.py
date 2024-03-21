from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api.db import movies, database


async def add_movie(payload: MovieIn):
    query = movies.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_movies():
    query = movies.select()
    return await database.fetch_all(query=query)


async def get_movie(id):
    query = movies.select(id=id)
    return await database.execute(query=query)


async def update_movie(id: int, payload: MovieIn):
    query = movies.update().where(id == id).values(**payload.dict())
    return await database.execute(query=query)
