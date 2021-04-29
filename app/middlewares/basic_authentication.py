from .base import ThryveBaseMiddleware
from flask import g, abort, request
# from app.modules.users.models import User
from app.modules.driver.models import Driver
from app.modules.restaurant.models import Restaurant


class BasicAuthenticationMiddleware(ThryveBaseMiddleware):
    def _process(self):
        """Attempts to parse and verify basic authentication credentials if they are
        included with this request.
        """

        auth = request.headers.get("Authorization")
        if not auth:
            return
        # Attempt email/password HTTP basic authorization.
        if auth.startswith("Basic "):
            auth = request.authorization
            email, password = auth["username"], auth["password"]
            is_driver = request.args.get("is_driver")
            request_ip = request.access_route[0]

            if is_driver:
                user = Driver.identify(email)

            else:
                user = Restaurant.identify(email)

            if not user:
                self.app.logger.warning(f"BAD EMAIL {email!r} from {request_ip}")
                abort(401, "Incorrect email or password.")
            if not user.verify_password(password):
                self.app.logger.warning(f"BAD PASSWORD for {email!r} from {request_ip}")
                abort(401, "Incorrect email or password.")

            g.user = user
