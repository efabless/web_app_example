from . import app

from flask import make_response, send_file, session, jsonify, request, render_template
import json
import time

value = 0


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/some_function', methods=['GET', 'POST'])
def do_some_function():
    # this is a server side api to do some function returning value
    value = time.localtime().tm_sec # seconds
    result = jsonify(value)
    return result
