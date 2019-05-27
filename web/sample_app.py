#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

#@app.route('/hello/<string:text>')
#@app.route('/hello')
#def hello_world(text=None):
#    return 'Just a plain text: "Hello from Flask!"' + (' With param ' + text if text else '')


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


@app.route('/', methods = ['GET'])
def hello_name():
    if request.method == 'GET':
        a=request.args.get('a')
        b=request.args.get('b')

    c = ""
    if a == None or b == None:
        a = 0
        b = 0
        c = "Не введены параметры"
    
    if c == "":
        result = str(gcd(int(a), int(b)))
    else:
        result = c

    return flask.render_template(
        'gcd.html',
        name=result,
    )

if __name__ == '__main__':
   app.run(debug = True)
