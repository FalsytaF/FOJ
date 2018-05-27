import os
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from problempage import md2html
from user import User, RegisterForm
from usermanage import register_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/FOJ'

db = SQLAlchemy(app)
db.create_all()

bcrypt = Bcrypt(app)

cdir = os.getcwd()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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


@app.route('/logincheck', methods=['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']

    real_password_hash = User.query.filter_by(username=username).first()
    return bcrypt.check_password_hash(real_password_hash, password)


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password = form.password.data
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = register_user(username=form.username.data,
                             email=form.email.data,
                             password=password_hash,
                             display_name=form.display_name.data,
                             school=form.school.data)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(port=2333, debug=True)
