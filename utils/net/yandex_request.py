from flask import Flask, request, jsonify, redirect
from requests import post

import sys

from urllib.parse import urlencode

client_id = 'fa9f01c6e9bb4492b9166b64c7ff8c0d'
client_secret = '87c8af70c3504363a867cdd08717470a'
baseurl = 'https://oauth.yandex.ru/'

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('code', False):
        print(request.args)
        print(request.data)
        print("code: " + request.args.get('code'))
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': client_id,
            'client_secret': client_secret
        }
        data = urlencode(data)
        return jsonify(post(baseurl + "token", data).json())
    else:
        return redirect(baseurl + "authorize?response_type=code&client_id={}".format(client_id))


@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return "Shutdown.."


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def start_server():
    app.debug = False
    app.run(host='127.0.0.1', port=443)


#start_server()

