from flask import *
import requests


host = 'http://127.0.0.1:1060'
url = '/send_messages'
login_url = '/login'

errors = {
    '<Response [200]>': '200 - Ok',
    '<Response [400]>': '404 - NotFound'
}
username = input('Введи никнейм: ')
password = input('Введи пароль: ')
response = requests.post(
    host+login_url,
    json={'username': username, 'text': password}
)

while not response.json()['ok']:
    print('неверный пароль')
    print()
    username = input('Введи никнейм: ')
    password = input('Введи пароль: ')
    response = requests.post(
        host+login_url,
        json={'username': username, 'text': password}
    )

print('Доступ разрешён. Welcome!')

while True:
    text = input('Введи сообщение: ')

    response = requests.post(
        host+url,
        json={'username': username, 'text': text}
    )
    print(response, '\n')
