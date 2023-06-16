from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

API_KEY = "8084a43722b510b89d975a30e568eace"
api_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query="
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class RatingEditForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e,g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    done = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    done = SubmitField("Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()
    movie_no = len(movies)
    for i in range(movie_no):
        movies[i].ranking = movie_no-i
    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = RatingEditForm()
    movie = Movie.query.filter_by(id=movie_id).first()
    if form.validate_on_submit():
        movie.rating = form.data['rating']
        movie.review = form.data['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie)
    db.session.commit()
    movies = db.session.query(Movie).all()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movies = requests.get(api_url+form.data['title']).json()['results']
        return render_template('select.html', movies=movies)
    return render_template("add.html", form=form)


@app.route('/search/<int:movie_id>')
def searc(movie_id):
    movie_data = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8084a43722b510b89d975a30e568eace').json()
    new_movie = Movie(
        title=movie_data['title'],
        year=movie_data['release_date'].split('-')[0],
        description=movie_data['overview'],
        img_url=MOVIE_DB_IMAGE_URL+movie_data['poster_path']
    )
    db.session.add(new_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=movie_data['title']).first()
    return redirect(url_for('edit', movie_id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
