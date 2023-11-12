import flask

import settings

from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():

    app = flask.Flask(__name__)

    app.config.update(
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI
    )

    app.url_map.strict_slashes = False

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    print(f"Successfully loaded modules: {settings.ENABLED_MODULES}")

    print(f"App is up and running")

    socketio.init_app(
        app=app,
        cors_allowed_origins='*',
        logger=False
    )

    return app
