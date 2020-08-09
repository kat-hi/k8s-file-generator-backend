from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'Json sagt' : 'Hallo, I bims, der Json'})