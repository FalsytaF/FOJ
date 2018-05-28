from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import Email, DataRequired
from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(500), unique=False)
    display_name = db.Column(db.String(100), unique=False)


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[Email(), DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    display_name = StringField('display_name', validators=[DataRequired()])
    school = StringField('school', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])