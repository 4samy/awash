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


@food_request_api.route("/create-food-request")
class CreateNewFoodRequest(Resource):

    decorators = [requires_auth]

    def post(self):
        """Create a new food request"""

        data = request.get_json()
        print("create food: ", data)

        user = g.user

        if not data:
            abort(400, "Missing necessary food request data")

        try:
            food_request = {}
            food_request["restaurant_id"] = user.id
            food_request["food_type"] = data["food_type"]
            food_request["food_quantity"] = data["food_quantity"]
            food_request["pickup_time"] = data["pickup_time"]

        except KeyError:
            abort(400, "Missing necessary data")

        new_food_request = FoodRequest(food_request)

        db.session.add(new_food_request)
        db.session.commit()

        return make_response(f"New Food Request successfully created", 200)


@food_request_api.route("/update-status")
class UpdateStatus(Resource):

    decorators = [requires_auth]

    def put(self):
        """Update Status of a food request"""

        data = request.get_json()
        print("status update: ", data)

        user = g.user

        if not data:
            abort(400, "Missing status update")

        if "status_update" not in data.keys():
            abort(400, "Missing status update")

        food_request = FoodRequest.query.filter_by(
            delivered=False
        ).filter_by(driver_id=user.id).first()

        if not food_request:
            abort(400, "Could not find food request for this driver")

        food_request.status = data["status_update"]

        db.session.commit()

        return make_response(f"Food Request for restaurant {food_request.restaurant.name} updated", 200)


@food_request_api.route("/complete-delivery")
class DeliverFoodRequest(Resource):

    decorators = [requires_auth]

    def put(self):
        """Update delivered status of food request"""

        user = g.user

        food_request = FoodRequest.query.filter_by(
            delivered=False
        ).filter_by(driver_id=user.id).first()

        if not food_request:
            abort(400, "Could not find food request for this driver")

        food_request.delivered = True

        db.session.commit()

        return make_response(f"Food Request for restaurant {food_request.restaurant.name} completed", 200)

