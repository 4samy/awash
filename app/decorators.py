import functools

from flask import g

from app.extensions.api import abort
import settings


def requires_auth(f):
    """Decorator for enforcing authentication. Flask's `g` global object is set
    to keep track of the currently authenticated user if credentials are given.
    See app.decorators for details.

    Flask globals are only valid for the active request.

    Regarding the semantics of variables:
        `g.user` and `user` refers to the user authenticating this request.
        `owner` refers to the user who owns the resource being requested.

    These may be equivalent to each other in some cases, but not always.
    If require_auth passes through, g.user is guaranteed to be set.
    """

    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.get("user"):
            raise abort(401, "Authentication required.")

        return f(*args, **kwargs)
    return decorated_function

