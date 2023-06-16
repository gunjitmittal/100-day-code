from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nbsaviyufvnbsidhov'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


class BookForm(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired()])
    submit = SubmitField('Submit', )


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book = Books(title=form.data['title'], author=form.data['author'], rating=form.data['rating'])
        db.session.add(book)
        db.session.commit()
        all_books = db.session.query(Books).all()
        return render_template('index.html', books=all_books)
    return render_template('add.html', form=form)


@app.route('/edit/<int:book_id>', methods=["GET", "POST"])
def edit(book_id):
    book = Books.query.filter_by(id=book_id).first()
    if request.method == 'POST':
        book.rating = request.form['rating']
        all_books = db.session.query(Books).all()
        db.session.commit()
        return render_template('index.html', books=all_books)
    return render_template('edit.html', book=book)


@app.route('/dele/<int:book_id>')
def dele(book_id):
    book = Books.query.filter_by(id=book_id).first()
    db.session.delete(book)
    db.session.commit()
    all_books = db.session.query(Books).all()
    return render_template('index.html', books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

