from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=False)
    password = db.Column(db.String(500), unique=False, nullable=False)
    display_name = db.Column(db.String(100), unique=False, nullable=False)
    school = db.Column(db.String(100), unique=False, nullable=False)
