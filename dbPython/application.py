from fastapi import FastAPI
import models
import database
app = FastAPI()\

@app.get('/')
async def sayHello():
    return {'success':'Hello'}

@app.post('/createMovie',response_model=models.Movie)
async def createMovie(movie:models.MovieCreate):
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id,**movie.dict())

@app.get('/readMovie',response_model=list)
async def read_movie():
    return database.read_movie()


@app.get('/readMovie/{movie_id}',response_model=models.Movie)
def read_movie(movie_id:int):
    movie = database.read_one_movie(movie_id)
    if movie is None:
        return 'Error'
    return movie

@app.put('/movies/{movie_id}',response_model=bool)
async def update_movie(movie_id:int,movie:models.Movie):
    updated = database.update_movie(movie_id,movie)
    if not updated:
        return 'Error'
    return models.Movie(id=movie_id,**movie.dict())

@app.delete('/movies/{movie_id}',response_model=dict)
async def remove_movie(movie_id:int):
    deleted = database.delete_movie(movie_id)
    if not deleted:
        return 'Failed'
    return {'success':'TRUE'}
@app.get('/testing')
async def see_test():
    return database.testing()