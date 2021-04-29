from flask_restplus import Namespace

from app.extensions import api


auth_api = Namespace(
    "auth", path="/auth",
    description="Client authentication"
)


def init_app(app):
    from . import resources  # noqa: F401
    api.add_namespace(auth_api)

