from app.extensions.api import api
import settings

def init_app(app, **kwargs):
    api.init_app(app)
