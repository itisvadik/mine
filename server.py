from flask import *
from time import *


app = Flask(__name__)
owner = 'Vad'
server_start_time = time()
app.config['SECRET_KEY'] = 'fdfdssf121211'
users = [
    {"username": "vad", 'password': '1234', 'is_admin': True},
    {"username": "dav", 'password': '4321', 'is_admin': False},
]


@app.route('/')
def start():
    return f'''
<html>
  <head>
    <title>Домашняя страница</title>
  </head>
  <body>
    <h1>Добро пожаловать на мой уютный сайт</h1>
    <h3><a target=_blank href={url_for('index')}>/index</a></h3>
    <h3><a target=_blank href={url_for('status')}>/status</a></h3>
  </body>
</html>
'''


@app.route('/index')
def index():
    username = 'Vad'
    return render_template('index.html', username=username)


@app.route('/index/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/index/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/index_base')
def index_base():
    return render_template('index_base.html')


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/tech/status')
def status():
    return {
        'status': 'Ok',
        'name': f'Messanger by {owner}',
        'server_start_time': ctime(server_start_time),
        'current-time': ctime(time())
    }


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('profile', username=session['logged_in']))

    if request.method == 'POST':
        for user in users:
            if request.form['username'] == user['username']:
                if request.form['password'] == user['password']:
                    session['logged_in'] = user['username']
                    return redirect(url_for('profile', username=session['logged_in']))
                else:
                    flash('Неправильный пароль', category='error')
                    break
            else:
                flash('Неправильный логин', category="error")
    
    return render_template('login.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for item in request.form:
            print(item, request.form[item])
    return render_template('form.html')


@app.route('/profile/<username>')
def profile(username):
    for user in users:
        if user['username'] == username:
            if 'logged_in' in session:
                if session['logged_in'] == username:
                    return render_template('profile.html', username=username)
                else:
                    abort(403)
        flash('Вам туда нельзя. Залогинтесь', category="error")
        return redirect(url_for("login"))
    abort(404)


if __name__ == '__main__':
    app.run(port=1060, debug=True)
