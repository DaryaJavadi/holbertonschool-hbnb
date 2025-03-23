from flask_restx import Namespace

# Create the v1 API namespace
api = Namespace('v1', description='Version 1 of the API')

# You can add further endpoints here

from flask import Blueprint
api = Blueprint('api', __name__)
from app.part2.api.v1 import users, reviews, amenities, cities, countries

from . import users
from . import reviews
from . import amenities
from . import cities
from . import countries
