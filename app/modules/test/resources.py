import settings
from . import test_api
from flask_restplus import Resource

@test_api.route("/")
class TestApiEndpoint(Resource):

    def get(self):
        print("Test endpoint successfully reached")

        return "Success"
