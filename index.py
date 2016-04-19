import os
import json

from flask import Flask, request
from player import Player

app = Flask(__name__)

@app.route('/')
def index():
  return '200 OK'

@app.route('/version', methods=['GET'])
def version():
  return Player().VERSION

@app.route('/bet', methods=['POST'])
def bet():
  return str(Player().bet(request.json))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
