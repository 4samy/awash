from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import restaurant_api
from .models import Restaurant
from app.modules.driver.models import Driver
from app.decorators import requires_auth


@restaurant_api.route("/create-new-restaurant")
class CreateRestaurant(Resource):

    def post(self):
        """Add new Restaurant object to database"""

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
                new_user = Restaurant(**data)
                pass
                db.session.add(new_user)
                db.session.commit()

                print(f"Restaurant '{email}' successfully created")

        else:
            abort(400, 'Missing email')

        return make_response(f"Restaurant {email} account successfully created", 200)

