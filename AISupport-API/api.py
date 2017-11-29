#!venv/Scripts/python
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
import os

app = Flask(__name__)

tasks = [
    {
        'msg': 'This message was sent by the API :D Yay!'
    }
]


@app.route('/test', methods=['GET'])
def get_tasks():
    resp = make_response('', 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    if os.name == 'nt':
        app.run(debug=True, threaded=True)
    else:
        app.run(host='0.0.0.0', threaded=True)
