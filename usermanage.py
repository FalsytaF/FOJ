from user import User
from flask_sqlalchemy import SQLAlchemy
from common import db

def register_user(username, email, password, display_name, school):
    user = User(username=username, email=email, password=password, display_name=display_name, school=school)
    db.session.add(user)
    db.session.commit()
    return user
