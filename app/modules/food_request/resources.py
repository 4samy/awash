from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import food_request_api
from .models import FoodRequest
from app.modules.restaurant.models import Restaurant
from app.modules.driver.models import Driver
from app.decorators import requires_auth


@food_request_api.route("/get-all")
class GetAllFoodRequests(Resource):

    def get(self):
        """Get all food requests in database"""

        food_requests = FoodRequest.query.all()
        print("all food requests: \n", food_requests)

        resp = {
            "food_requests": food_requests,
            "message": "Successful get of all food requests"
        }
        return resp, 200
