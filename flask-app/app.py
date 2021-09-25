#!/usr/bin/python3
from flask import Flask, request
import time
import string
import random

app = Flask('My first app')


@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"


@app.route("/whoami")
def whoami():
    browser = request.user_agent.browser
    ip_address = request.remote_addr
    current_time = time.strftime('%A %B, %d %Y %H:%M:%S')
    return "<ul>" \
           f'<li>Браузер <b>{browser}</b></li>' \
           f'<li>IP-Address: <b>{ip_address}</b></li>' \
           f'<li>Текущее время на сервере <b>{current_time}</b></li>' \
           "</ul>"


@app.route("/source_code")
def source_code_page():
    import inspect
    return inspect.getsource(inspect.getmodule(inspect.currentframe()))


@app.route("/random")
def random_page():
    length = get_query_key(request.args, 'length')
    specials = get_query_key(request.args, 'specials')
    digits = get_query_key(request.args, 'digits')

    return "<h2>Введите query параменты </h2>" \
           "<ul>" \
           '<li>length <b>0-100</b></li>' \
           '<li>specials <b>1 или 0</b></li>' \
           '<li>digits <b>1 или 0</b></li>' \
           "</ul>" \
           f'<div>Рандомная строка: {get_random_letters(length, specials, digits)}</div>'


def get_query_key(arguments, key):
    if key in arguments:
        return arguments[key]
    return 0


def get_random_letters(length=0, specials=0, digits=0):
    new_string = string.ascii_letters
    specials_char = "!@%/()=?+.-"

    if is_on_params(specials):
        new_string = new_string + specials_char

    if is_on_params(digits):
        new_string = new_string + string.digits

    print(new_string)
    return ''.join(random.choice(new_string) for i in range(get_available_length(length)))


def is_on_params(param):
    if int(param) == 1:
        return True

    return False


def get_available_length(number):
    if int(number) > 100:
        return 100
    elif int(number) < 0:
        return 0

    return int(number)


if __name__ == '__main__':
    app.run(debug=True)
