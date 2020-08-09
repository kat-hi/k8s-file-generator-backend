import json

from flask import Flask, jsonify, request
from reportlab.lib import yaml
from .utils import is_hostname_already_used
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'Json sagt' : 'Hallo, I bims, der Json'})

@app.route('/convert/deployment/', methods=['POST'])
def convert_deployment():
    response = json.loads(request.data.decode('utf-8'))
    return yaml.dump(response, default_flow_style=False)


@app.route('/check/ingress', methods=['GET'])
def get_current_ing():
    data = json.loads(request.data.decode('utf-8'))
    if is_hostname_already_used(data.hostname):
        return jsonify({'data': True})
    else:
        return jsonify({'data': False})