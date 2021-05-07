from flask import g, request, make_response
from flask_restplus import Resource

from app.extensions import db
from app.extensions.api import abort

from . import driver_api
from .models import Driver
from app.decorators import requires_auth


@driver_api.route("/create-new-driver")
class CreateDriver(Resource):

    def post(self):
        """Add new Driver object to database"""

        data = request.json
        if 'email' in data.keys():
            email = data['email']
            if Driver.query.filter_by(email=email).scalar():
                abort(400, f"User with email '{email}' already exists")
            else:
                new_user = Driver(**data)
                db.session.add(new_user)
                db.session.commit()

                print(f"User '{email}' successfully created")

        else:
            abort(400, 'Missing email')

        return make_response("Success", 200)


@driver_api.route("/info")
class DriverObject(Resource):

    decorators = [requires_auth]

    def get(self):
        """Get driver object"""

        user = g.user

        print(user)

        return user.id

