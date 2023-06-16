from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap(app)


# #CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField('Login')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    print(request.method)
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if not user:
            new_user = User(
                name=request.form['name'],
                email=request.form['email'],
                password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(name=request.form['name']).first()
            return redirect(url_for('secrets', user_id=user.id, logged_in=current_user))
        else:
            flash("Email already exists")
    return render_template("register.html")


@app.route('/login', methods=["POST", 'GET'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.data['email']).first()
        if user is None:
            error = "Email not registered"
        else:
            if check_password_hash(user.password, form.data['password']):
                login_user(user)
                return redirect(url_for('secrets', user_id=user.id, logged_in=current_user))
            else:
                error = "Invalid Password"
    if error:
        flash(error)
    return render_template("login.html", form=form, logged_in=current_user)


@app.route('/secrets/<user_id>')
@login_required
def secrets(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template("secrets.html", username=user.name, logged_in=current_user)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
@login_required
def download():
    return send_from_directory("static/files", 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
