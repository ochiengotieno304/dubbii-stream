import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'


@app.route('/')
def index():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return render_template('index.html', movies=movies)


@app.route('/<int:movie_id>')
def movie(movie_id):
    movie = get_movie(movie_id)
    return render_template('movie.html', movie=movie)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        genre = request.form['genre']

        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO movies (title, link, genre) VALUES (?, ?, ?)', (title, link, genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')
