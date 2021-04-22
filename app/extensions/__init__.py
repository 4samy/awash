import flask_cors
import flask_migrate
import flask_sqlalchemy

import settings

cors = flask_cors.CORS()

db = flask_sqlalchemy.SQLAlchemy()

migrate = flask_migrate.Migrate()

from .api import api

def init_app(app):

    print("extensions init")

    extensions = (
        cors,
        db
    )

    for extension in extensions:
        extension.init_app(app)

    migrate.init_app(app, db)
    extensions = extensions + (migrate,)

    extension_names = [x.__class__.__name__ for x in extensions]

    app.logger.info(f"Successfully loaded extensions: {extension_names}")

