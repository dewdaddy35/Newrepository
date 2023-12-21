#!/user/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.getroute("/")
def hello():
    return "<h1>Hello, World</h1>"