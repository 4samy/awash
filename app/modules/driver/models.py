import settings

import bcrypt
import itsdangerous

from flask import abort

from app.extensions import db
from app.jwt import generate_token, validate_token


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    password = db.Column(db.LargeBinary(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    car_description = db.Column(db.Text, nullable=True)
    reward_points = db.Column(db.Integer, nullable=False, default=0)
    food_requests = db.relationship('FoodRequest', backref="driver", lazy=True)

    def __init__(self, **kwargs):
        super(Driver, self).__init__(**kwargs)

        self.email = self.email.strip()
        self.first_name = self.first_name.strip()
        self.password = bcrypt.hashpw(
            self.password.encode(), bcrypt.gensalt()
        )

    def __repr__(self):
        return f"<Driver id: {self.id} {self.email}>"

    def verify_password(self, password):
        """Returns True if this password matches for this User."""

        if isinstance(password, str):
            password = password.encode()

        if bcrypt.checkpw(password, self.password):
            return True

        return False

    def gen_access_token(self, exp=None):
        """Returns JWT token for this User"""

        if not exp:
            exp = settings.TOKEN_TYPES["session"]["expires_in"]

        payload = {
            "driver_id": self.id,
            "is_driver": True
        }
        token = generate_token(payload, "session", expires_in=exp)

        return {
            "access_token": token,
            "expires_in": exp
        }

    @staticmethod
    def verify_access_token(access_token):
        """Returns the User for this access_token if it passes verification"""

        try:
            payload = validate_token(access_token)
        except itsdangerous.BadSignature:
            abort(401, "Invalid token")

        return payload

    @staticmethod
    def identify(user_identity):
        """Returns a User object corresponding with this username or email or id"""

        if isinstance(user_identity, int):
            return Driver.query.get(user_identity)

        return Driver.query.filter(
            Driver.email.ilike(user_identity)
        ).first()
