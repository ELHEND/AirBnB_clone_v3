#!/usr/bin/python3
"""
view for the states
"""

from flask import abort, request, make_response, jsonify
from api.v1.views import app_views
from models import storage
from models.base_model import BaseModel
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """Retrieves all state objects"""
