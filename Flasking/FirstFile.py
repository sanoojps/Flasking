# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:26:08 2018

@author: sanooj
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world!<h1>"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!<h1>' %(name)

#run
    if __name__ == '__main__':
        app.run(debug=True)
    