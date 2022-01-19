from flask import *
from time import *

app = Flask(__name__)
owner = 'Vad'
server_start_time = time()

# структура сообщения: username, text, timestamp
messages = [
    {'username': 'Ваня М.', 'text': 'Привет', 'timestamp': time()},
    {'username': 'Миша Б.', 'text': 'Здаров', 'timestamp': time()},
    {'username': 'Ваня М.', 'text': 'Классный мессанджер, скажи?', 'timestamp': time()}
]
users = [
    {'username': 'Ваня М.', 'password': '12345'},
    {'username': 'Миша Б.', 'password': '54321'}
]


@app.route('/')
def hello():
    return f'''
<h1>Добро пожаловать в мой уютный мессенджер :)</h1>
<h3><a target='_blank' href={url_for('status')}>/status</a></h3>
<h3><a target='_blank' href=/get_messages>/get_messages</a></h3>
'''


# <h3><a target='_blank' href=/send_messages>/send_messages</a></h3>


@app.route('/tech/status')
def status():
    return {
        'status': 'Ok',
        'name': f'Messanger by {owner}',
        'server_start_time': ctime(server_start_time),
        'current-time': ctime(time()),
        'messages': len(messages),
    }


@app.route('/get_messages')
def get_messages():
    return {
        'messages': messages
    }


@app.route('/send_messages', methods=['get', 'post'])
def send_messages():
    username = request.json['username']
    text = request.json['text']
    messages.append(
        {
            'username': username,
            'text': text,
            'timestamp': time()
        }
    )

    return {
        'ok': True
    }


@app.route('/login', methods=['post'])
def login():
    username = request.json['username']
    password = request.json['password']
    login_ok = False

    for user in users:
        if user['username'] == username:
            if password['password'] == password:
                login_ok: True
                break
    return {'ok': login_ok}


if __name__ == '__main__':
    app.run(port=1060, debug=True)
