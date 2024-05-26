#!/usr/bin/python3
"""Flask app"""

from flask import Flask
from os import getenv
from models import storage
from flask import jsonify

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Close session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', 5000)
    port = getenv('HBNB_API_PORT', '0.0.0.0')
    app.run(host=host, port=int(port), threaded=True)
