from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import food_request_api
from .models import FoodRequest
from app.modules.restaurant.models import Restaurant
from app.modules.driver.models import Driver
from app.decorators import requires_auth

from .schemas import FoodRequestSchema


@food_request_api.route("/get-all")
class GetAllFoodRequests(Resource):
    schema = FoodRequestSchema()

    def get(self):
        """Get all food requests in database"""

        food_requests_list = []

        food_requests = FoodRequest.query.all()
        # food_requests = FoodRequest.query.get(1)
        print("all food requests: \n", food_requests)

        # print("food restaurant: ", food_requests.restaurant)

        for food in food_requests:
            dump = self.schema.dump(food).data
            print(dump)
            food_requests_list.append(dump)

        resp = {
            "food_requests": food_requests_list,
            "message": "Successful get of all food requests"
        }
        return resp, 200


# @food_request_api.route("/create-food-request")
# class CreateNewFoodRequest(Resource):

#     decorators = [requires_auth]

#     def get(self):

#         print(g.user.id)

#         return

#     def post(self):
#         """Create a new food request"""

#         data = request.get_json()
#         print("create food: ", data)

#         user = g.user



#         if not data:
#             abort(400, "Missing necessary food request data")


