from flask_restplus import Namespace

from app.extensions import api


food_request_api = Namespace(
    "food_request", path="/food_request",
    description="Endpoint for all food request data"
)


def init_app(app):
    from . import resources, models  # noqa: F401
    api.add_namespace(food_request_api)

