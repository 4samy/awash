from flask_restplus import Namespace

from app.extensions import api


test_api = Namespace(
    "test", path="/test",
    description="test endpoint"
)

def init_app(app):
    from . import resources
    api.add_namespace(test_api)

