# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 06:51:49 2018

@author: sanooj
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)


if __name__ == '__main__':
     app.run(debug=True)


# =============================================================================
# from flask.ext.script import Manager
# manager = Manager(app)
# 
# 
# if __name__ == '__main__':
#     manager.run()
# =============================================================================


from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)