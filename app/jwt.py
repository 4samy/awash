from flask import current_app

import settings
import itsdangerous


def get_serializer(secret_key=None, expires_in=None, salt=None):
    """Returns a time-sensitive JWT serializer.

    Args:
        secret_key: The signing key. By default, Flask's SECRET_KEY is used.
        expires_in: Duration of time in seconds that generated tokens will be
                    valid. Default defers to itsdangerous.
        salt: A unique string included in the signing key to restrict usage of
              tokens with identical payload. Default defers to itsdangerous.
    """

    if not secret_key:
        secret_key = settings.SECRET_KEY

    return itsdangerous.TimedJSONWebSignatureSerializer(
        secret_key,
        expires_in=expires_in,
        salt=salt
    )


def generate_token(payload, context, secret_key=None, expires_in=None):
    """Returns a JWT containing the `payload` signed using Flask's `SECRET_KEY`
    and the salt for the given `context`.

    Args:
        payload: Data payload to be JSON serialized.
        context: Definition of essential token details (e.g., expiration time,
                 salt, etc.) While expiration time is not required, the salt
                 is always necessary to prevent users from reusing signed
                 tokens for cases outside their intended use.
        secret_key: The signing key. Default defers to `get_serializer()`.
        expires_in: Duration of time in seconds generated tokens will be valid.
    """

    context_details = settings.TOKEN_TYPES.get(context)

    if not context_details:
        raise ValueError(f"'{context}' is not a valid token context")

    expires_in = expires_in or context_details.get("expires_in")
    salt = context_details.get("salt")

    serializer = get_serializer(secret_key, expires_in=expires_in, salt=salt)
    token = serializer.dumps(payload)
    token_utf8 = token.decode("utf-8")

    return f"{salt}:{token_utf8}"


def _extract_parts(token):
    """Returns the salt and JWT components of `token` as a tuple."""

    parts = token.split(":")
    if len(parts) == 1:
        return (None, parts[0])

    salt, jwt = parts
    return (salt, jwt)


def is_token_valid(token):
    """Returns True if `token` validates successfully. Else, False."""

    salt, jwt = _extract_parts(token)
    serializer = get_serializer(salt=salt)
    try:
        serializer.loads(jwt)
    except (itsdangerous.BadSignature):
        return False

    return True


def validate_token(token, return_header=False):
    """Returns the payload inside `token` if validation is successful. Throws
    an exception about the error otherwise."""

    salt, jwt = _extract_parts(token)

    serializer = get_serializer(salt=salt)
    try:
        ret = serializer.loads(jwt, return_header=return_header)
    except itsdangerous.SignatureExpired as err:
        current_app.logger.warn(f"[JWT] Expired token: {token}")
        raise
    except itsdangerous.BadSignature as err:
        current_app.logger.warn(f"[JWT] Bad token: {token}")
        raise

    return ret

