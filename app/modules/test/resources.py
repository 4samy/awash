import settings
from . import test_api
from flask_restplus import Resource

from app.decorators import requires_auth


@test_api.route("/")
class TestApiEndpoint(Resource):

    decorators = [requires_auth]

    def get(self):
        print("Test endpoint successfully reached")

        return "Success"
