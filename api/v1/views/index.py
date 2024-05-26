#!/usr/bin/python3
"""Flask app"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Return stats"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    count_dict = {}
    for key, value in classes.items():
        count_dict[key] = storage.count(value)
    return jsonify(count_dict)
