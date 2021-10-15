#!/usr/bin/python3
from flask import Flask, request
import time
import string
import random

app = Flask('My first app')


def bootstrap_template(content):
    return f"""
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

            <title>Flask App</title>
          </head>
          <body>
            <header>
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">Flask App</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="/whoami">Whoami</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="/random">Random</a>
                        </li>
                      </ul>
                    </div>
                  </div>
                </nav>
            </header>  
            <div class="container">    
                {content}
            <div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
          </body>
        </html>
    """


@app.route("/")
def home():
    content = """
        <div class="card" style="width: 18rem; margin: 20px auto;">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Flask App</h5>
            <p class="card-text">My first flask app</p>
            <a target="_blank" href="https://flask.palletsprojects.com/en/2.0.x/" class="btn btn-primary">Flask documentation</a>
          </div>
        </div>
        """
    return bootstrap_template(content)


@app.route("/whoami")
def whoami():
    browser = request.user_agent.browser
    ip_address = request.remote_addr
    current_time = time.strftime('%A %B, %d %Y %H:%M:%S')

    content = f"""
                <ul class="list-group list-group-flush">
                   <li class="list-group-item">Браузер <b>{browser}</b></li>
                   <li class="list-group-item">IP-Address: <b>{ip_address}</b></li>
                   <li class="list-group-item">Текущее время на сервере <b>{current_time}</b></li>
               </ul>
            """
    return bootstrap_template(content)


@app.route("/source_code")
def source_code_page():
    import inspect
    return inspect.getsource(inspect.getmodule(inspect.currentframe()))


@app.route("/random")
def random_page():
    length = get_query_key(request.args, 'length')
    specials = get_query_key(request.args, 'specials')
    digits = get_query_key(request.args, 'digits')

    content = f"""
                <h2>Введите query параменты </h2>
                <ul class="list-group list-group-flush">
                   <li class="list-group-item">length <b>0-100</b</b></li>
                   <li class="list-group-item">specials <b>1 или 0</b></b></li>
                   <li class="list-group-item">digits <b>1 или 0</b></li>
               </ul>
               <div>Рандомная строка: {get_random_letters(length, specials, digits)}</div>
            """
    return bootstrap_template(content)


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