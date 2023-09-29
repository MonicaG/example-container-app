from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><center>Example app</center></h1>'

@app.route('/hello')
def hello():
    return '<h1><center>Hello!</center></h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)