from .base import ThryveBaseMiddleware
from flask import g, abort, request
# from app.modules.users.models import User
from app.modules.driver.models import Driver
from app.modules.restaurant.models import Restaurant


class JWTAuthenticationMiddleware(ThryveBaseMiddleware):

    def _extract_users_from_payload_to_context(self, payload):
        if "driver_id" in payload:
            user = Driver.identify(payload["driver_id"])
            if not user:
                abort(401)
            g.user = user
        elif "restaurant_id" in payload:
            user = Restaurant.identify(payload["restaurant_id"])
            if not user:
                abort(401)
            g.user = user

    def _process(self):
        """Attempts to verify jwt token if is included with this request.
        """
        auth = request.headers.get("Authorization")
        if not auth:
            return

        if auth.startswith("Bearer "):
            _, access_token = auth.split()
            self._extract_users_from_payload_to_context(
                Driver.verify_access_token(access_token)
            )
