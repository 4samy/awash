from flask_restplus import Namespace

from app.extensions import api


driver_api = Namespace(
    "driver", path="/driver",
    description="Endpoint for all driver data"
)


def init_app(app):
    from . import resources, models  # noqa: F401
    api.add_namespace(driver_api)

