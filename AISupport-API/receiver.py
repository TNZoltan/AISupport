#!venv/Scripts/python
from flask import Flask,  make_response, jsonify, request
from controller import concrete_command
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route('/api/talk', methods=['POST'])
@cross_origin()
def answer():
    data = request.get_json()
    message = concrete_command(data)
    resp = make_response(jsonify(message), 200)
    return resp


@app.route('/api/test', methods=['GET'])
def test():
    # simply send back an OK
    resp = make_response('', 200)
    return resp


if __name__ == '__main__':
    # if windows - run local
    if os.name == 'nt':
        app.run(debug=True, threaded=True)
    # if linux - also run on public
    else:
        app.run(host='0.0.0.0', threaded=True)
