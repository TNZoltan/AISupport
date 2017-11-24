#!venv/Scripts/python
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

app = Flask(__name__)

tasks = [
    {
        'msg': 'This message was sent by the API :D Yay!'
    }
]

@app.route('/test', methods=['GET'])
def get_tasks():

    resp = make_response(jsonify({'tasks': tasks}), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(debug=True)