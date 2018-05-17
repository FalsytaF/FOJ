from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problems')
def problem_page():
    return render_template('problems.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=2333, debug=True)