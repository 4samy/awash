import settings

from flask import current_app, request, abort
from flask_restplus import reqparse, Resource

from . import auth_api
from ..driver.models import Driver
from ..restaurant.models import Restaurant


@auth_api.route("")
class Authentication(Resource):

    def post(self):
        """Returns a JWT access token for this user. email/password
        authentication is strictly enforced; no other methods should work.
        """

        data = request.get_json()
        # data = request.data
        print("data: ", data)

        arg_parser = reqparse.RequestParser()
        arg_parser.add_argument(
            "exp",
            default=15552000,
            help="Parameter must be an integer",
            type=int
        )

        args = arg_parser.parse_args()

        print(args)

        auth = request.authorization
        print("auth req: ", auth)
        if not auth:
            # Try extracting from POST body
            print("here")
            auth = request.get_json()
            print("here")
            print("auth: ", auth)
            if not auth or not ("email" in auth and "password" in auth):
                abort(401, "Missing authentication credentials")

        # if auth["is_driver"]:
        #     # if it is a driver
        #     user = Driver.identify(auth["email"])
        #     password = auth["password"]

        # else:
        #     # If it is a restaurant
        #     user = Restaurant.identify(auth["email"])
        #     password = auth["password"]

        is_driver = True

        user = Driver.identify(auth["email"])
        password = auth["password"]

        if not user:
            user = Restaurant.identify(auth["email"])
            is_driver = False

        if not user or not user.verify_password(password):
            current_app.logger.warn(
                "Incorrect credentials for {} from {}".format(
                    auth["email"],
                    *request.access_route
                )
            )
            abort(401, "Incorrect email or password")

        access_token = user.gen_access_token(args["exp"])

        current_app.logger.info("[AUTH] User {} logged IN from {}".format(
            user.email,
            *request.access_route
        ))

        access_token.update({
            "is_driver": is_driver
        })

        # return resp, 200
        return access_token
