#!/usr/bin/python3
"""
return status of the page which we selected it
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def get_status():
    """In this route we retrive response status """
    return jsonify({
        'status': 'OK'
    })


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """In this route we retrieves the number of each objects by type"""

    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    })