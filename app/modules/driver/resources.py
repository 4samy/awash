from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import driver_api
from .models import Driver
from app.modules.restaurant.models import Restaurant
from app.decorators import requires_auth

from app.modules.food_request.models import FoodRequest
from app.modules.food_request.schemas import FoodRequestSchema

from .schemas import DriverSchema


@driver_api.route("/create-new-driver")
class CreateDriver(Resource):

    def post(self):
        """Add new Driver object to database"""

        data = request.get_json(force=True)
        print("request", request.get_json(force=True))
        print("data: ", data)
        if 'email' in data.keys():
            email = data['email']
            if Driver.query.filter_by(email=email).scalar():
                abort(400, f"Driver with email '{email}' already exists")
            if Restaurant.query.filter_by(email=email).scalar():
                abort(400, f"Restaurant with email '{email}' already exists")
            else:
                new_user = Driver(**data)
                db.session.add(new_user)
                db.session.commit()

                print(f"User '{email}' successfully created")

        else:
            abort(400, 'Missing email')

        return make_response(f"Driver {email} account successfully created", 200)


@driver_api.route("/info")
class GetDriverObject(Resource):

    decorators = [requires_auth]
    driver_schema = DriverSchema()
    food_request_schema = FoodRequestSchema()

    def get(self):
        """Get driver object"""

        user = g.user

        user_schema = self.driver_schema.dump(user).data

        food = FoodRequest.query.filter_by(driver_id=user.id).first()

        user_schema["food_request"] = {}

        if food:
            food_request = self.food_request_schema.dump(food).data

            user_schema["food_request"] = food_request

        print(f"Driver schema: {user_schema}")

        return user_schema


@driver_api.route("/update-info")
class UpdateDriverInfo(Resource):

    decorators = [requires_auth]

    def put(self):
        """Update driver data"""

        data = request.get_json()

        user = g.user

        try:

            if data["first_name"] != "":
                user.first_name = data["first_name"]
            if data["phone_number"] != "":
                user.phone_number = data["phone_number"]
            if data["car_description"] != "":
                user.car_description = data["car_description"]

        except KeyError:
            abort(400, "Missing info")

        db.session.commit()

        return make_response(f"Driver {user.first_name} successfully updated info", 200)
