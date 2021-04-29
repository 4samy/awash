from flask import current_app

from .api import Api

from .errors import abort  # noqa: F401


# Use customized version of the API extension.
api = Api(
    title="DonateFood REST API",
    version="1.0",
    # Disable the documentation from all env
    # TODO: will enable the swagger doc when adding authentication to the api url
    # doc=False
)
