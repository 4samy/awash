from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import rewards_api
from .models import Rewards
from app.modules.restaurant.models import Restaurant
from app.decorators import requires_auth


@rewards_api.route("/")
class GetRestaurantRewards(Resource):

    def get(self):
        return
