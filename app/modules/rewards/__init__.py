from flask_restplus import Namespace

from app.extensions import api

rewards_api = Namespace(
    "rewards", path="/rewards",
    description="Endpoint for all rewards"
)


def init_app(app):
    from . import resources, models  # noqa: F401
    api.add_namespace(rewards_api)

