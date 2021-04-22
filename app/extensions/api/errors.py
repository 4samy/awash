import flask
from werkzeug.exceptions import HTTPException


def abort(code=500, message=None, **kwargs):
    """
    Properly abort the current request.

    Raise a `HTTPException` for the given status `code`.
    Attach any keyword arguments to the exception for later processing.

    :param int code: The associated HTTP status code
    :param str message: An optional details message
    :param kwargs: Any additional data to pass to the error payload
    :raise HTTPException:
    """
    try:
        flask.abort(code)
    except HTTPException as e:
        if message:
            kwargs["message"] = str(message)
        if kwargs:
            # Format a list of validation errors returned by Marshmallow into a
            # simpler {"field": "message"} format.
            if "errors" in kwargs:
                for k, v in kwargs["errors"].items():
                    if isinstance(v, list):
                        kwargs["errors"][k] = v[0]

            e.data = kwargs
        raise
