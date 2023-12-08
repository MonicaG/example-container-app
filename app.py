from flask import Flask
from os import environ
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><center>Example app</center></h1>'

@app.route('/hello')
def hello():
    return '<h1><center>Hello! Hello!</center></h1>'

@app.route('/bye')
def hello():
    return '<h1><center>Goodbye!</center></h1>'

@app.route('/test')
def test():
    word = environ.get("APP_WORD")
    return f'<h1><center>Today\'s word is {escape(word)}</h1>'

if __name__ == "__main__":
    app_port = environ.get("APP_PORT")
    app.run(host="0.0.0.0", port=5050)