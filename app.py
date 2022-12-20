import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import tmdbsimple as tmdb
import os
import asyncio


tmdb.API_KEY = os.environ['api_key']


def get_db_connection():
    conn = sqlite3.connect("database.sqlite")
    conn.row_factory = sqlite3.Row
    return conn


def get_movie(movie_id):
    conn = get_db_connection()
    movie = conn.execute("SELECT * FROM movies WHERE id = ?",
                         (movie_id,)).fetchone()
    conn.close()
    if movie is None:
        abort(404)
    return movie


def get_movie_poster_and_overview(movie_id):
    movie = get_movie(movie_id)
    title = movie['title']
    search = tmdb.Search()
    response = search.movie(query=title)
    poster_path = response['results'][0]['poster_path']
    overview = response['results'][0]['overview']
    path = "http://image.tmdb.org/t/p/w500" + poster_path

    return [overview, path]


def get_movie_backdrop(movie_id):
    movie = get_movie(movie_id)
    title = movie['title']
    search = tmdb.Search()
    response = search.movie(query=title)
    backdrop_path = response['results'][0]['backdrop_path']
    backdrop_path = "http://image.tmdb.org/t/p/w500" + backdrop_path

    return backdrop_path


def movie_search(search):
    conn = get_db_connection()
    cusor = conn.cursor()
    cusor.execute("SELECT * FROM `movies` WHERE `title` LIKE ?",
                  ("%"+search+"%",))

    result = cusor.fetchall()
    conn.close
    return result


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = dict(request.form)
        movies = movie_search(data["search"])
    else:
        conn = get_db_connection()
        movies = conn.execute(
            'SELECT * FROM movies ORDER BY created DESC').fetchall()
        conn.close()

    app.jinja_env.globals.update(movie_data=get_movie_poster_and_overview)
    # app.jinja_env.globals.update(backdrop_image=get_movie_backdrop)

    return render_template('index.html', movies=movies)


@app.route('/movies/<int:movie_id>')
def movie(movie_id):
    movie = get_movie(movie_id)
    overview = get_movie_poster_and_overview(movie['id'])[0]
    poster = get_movie_poster_and_overview(movie['id'])[1]
    return render_template('movie.html', movie=movie, overview=overview, poster=poster)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        genre = request.form['genre']
        quality = request.form['quality']

        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO movies (title, link, quality, genre) VALUES (?, ?, ?, ?)', (title, link, quality, genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/movies/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    movie = get_movie(id)

    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        genre = request.form['genre']
        quality = request.form['quality']

        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute(
                'UPDATE MOVIES SET title = ?, link = ?, genre = ?, quality = ?,  WHERE id = ?', (title, link, genre, quality, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)


@app.route('/movies/<int:id>/delete', methods=['POST'])
def delete(id):
    movie = get_movie(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('success', f"Movie deleted successfully {movie['title']}")
    return redirect(url_for('index'))
