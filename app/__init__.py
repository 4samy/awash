import flask
import logging
import settings

from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(log_info=True, **kwargs):

    app = flask.Flask(__name__, **kwargs)

    app.config.update(
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=settings.SQLALCHEMY_TRACK_MODIFICATIONS
    )

    app.url_map.strict_slashes = False

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    # app.logger.setLevel(logging.INFO)

    app.logger.info("Successfully loaded modules: {}".format(
        settings.ENABLED_MODULES
    ))

    app.logger.info("App is up and running!")

    socketio.init_app(
        app=app,
        cors_allowed_origins='*',
        logger=True
    )

    return app
