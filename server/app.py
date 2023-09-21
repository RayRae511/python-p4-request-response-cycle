#!/usr/bin/env python3
from flask import Flask,request, current_app, g
import os


app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
               <h2>The app name is called {appname}</h2>
               <h3>The path of this app on my PC is: {g.path}</h3>'''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
