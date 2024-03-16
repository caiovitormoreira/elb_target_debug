import time
import logging
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy #for the database crud stuff

app = Flask(__name__)

#================================ / ==========================================
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def headers():
    headers = dict(request.headers)
    return jsonify(headers)

#================================ /healthcheck ================================
@app.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({'health':'1'})
