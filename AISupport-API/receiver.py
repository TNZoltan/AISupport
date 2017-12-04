#!venv/Scripts/python
from flask import Flask
from flask import jsonify
from flask import request
from controller import concrete_command
from flask import make_response
import os

app = Flask(__name__)


@app.route('/api/talk', methods=['PUT, OPTIONS'])
def answer():
    message = concrete_command(request.data)
    message = 'boii'
    resp = make_response(jsonify(message), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/api/test', methods=['GET'])
def test():
    # simply send back an OK
    resp = make_response('', 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    # if windows - run local
    if os.name == 'nt':
        app.run(debug=True, threaded=True)
    # if linux - also run on public
    else:
        app.run(host='0.0.0.0', threaded=True)
