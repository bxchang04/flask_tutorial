from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'py - 3 - m venv venv
