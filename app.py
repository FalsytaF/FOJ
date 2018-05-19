import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from problempage import md2html

app = Flask(__name__)
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
    #print(cdir)
    with open(decr_file, 'r') as fp:
        decr_md = fp.read()
    decr_html = md2html(decr_md)

    return decr_html
    #return render_template('problem.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=2333, debug=True)