from flask_restplus import Namespace

from app.extensions import api


restaurant_api = Namespace(
    "restaurant", path="/restaurant",
    description="Endpoint for all restaurant data"
)


def init_app(app):
    from . import resources, models  # noqa 401
    api.add_namespace(restaurant_api)

