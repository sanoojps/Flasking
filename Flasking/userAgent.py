# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 06:05:39 2018

@author: sanooj
"""

from flask import Flask
app = Flask(__name__)


#using context
from  flask import request

@app.route("/")
def index():
    user_agent = request.headers.get('User-Agent')
    #print(request.headers)
    return "<p> Your Browser is %s <p>" %(user_agent)


#run
if __name__ == '__main__':
    app.run(debug=True)