import os
from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from problempage import md2html
from user import User
from usermanage import register_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/FOJ'

db = SQLAlchemy(app)
db.create_all()

bcrypt = Bcrypt(app)

cdir = os.getcwd()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/problems')
def problem_list():
    return render_template('problems.html')

@app.route('/problem/<pid>')
def problem_page(pid):
    problem_path = os.path.join(cdir, 'static', 'problems', str(pid))
    decr_file = os.path.join(problem_path, 'decr.md')
    with open(decr_file, 'r') as fp:
        decr_md = fp.read()
    decr_html = md2html(decr_md)

    return decr_html
    #return render_template('problem.html')

@app.route('/createuser', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    school = request.form['school']

    password = bcrypt.generate_password_hash(password).decode('utf-8')

    register_user(username=username, email=email, password=password, display_name=display_name, school=school)

@app.route('/logincheck', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']

    real_password_hash = User.query.filter_by(username=username).first()
    return bcrypt.check_password_hash(real_password_hash, password)


@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=2333, debug=True)