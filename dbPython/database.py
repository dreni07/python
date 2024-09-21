import sqlite3
import models

def create_connection():
    connection = sqlite3.connect('movies.db')
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
    create table if not exists movies(
        id integer primary key autoincrement,
        title text not null,
        director text not null);
    ''')
    connection.commit()
    connection.close()

create_table()

def create_movie(movie:models.MovieCreate):
    connection = create_connection()
    cursori = connection.cursor()
    cursori.execute('''
    insert into movies (title,director) values (?,?)
    ''',(movie.title,movie.director))
    connection.commit()
    movie_id = cursori.lastrowid
    connection.close()
    return movie_id


def read_movie():
    connection = create_connection()
    cursori = connection.cursor()
    cursori.execute('''
    select * from movies;
    ''')
    connection.commit()
    rows = cursori.fetchall()
    movies = [models.Movie(id=row[0],title=row[1],director=row[2]) for row in rows]
    connection.close()
    return movies

def testing():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        select * from movies;
    ''')
    connection.commit()
    rows = cursor.fetchall()
    return rows

def read_one_movie(movieId:int):
    connection = create_connection()
    cursori = connection.cursor()
    cursori.execute("SELECT * FROM MOVIES WHERE id = ?;",(movieId))
    connection.commit()
    row = cursori.fetchone()
    connection.close()
    if row is None:
        return None
    return models.Movie(id=row[0],title=row[1],director=row[2])

def update_movie(movieId:int,movie:models.Movie):
    connection = create_connection()
    cursori = connection.cursor()
    cursori.execute("update movies set id=?,title=?,director=? where movieId = ?;",(movie.title,movie.director,movie.id,movieId))
    connection.commit()
    updated = cursori.rowcount
    connection.close()
    return updated > 0

def delete_movie(movieId:int):
    connection = create_connection()
    cursori = connection.cursor()
    cursori.execute("delete from movies where id=?",(movieId))
    connection.commit()
    delete = cursori.rowcount
    connection.close()
    return delete>0



