import settings

import bcrypt
import itsdangerous

from flask import abort

from app.extensions import db
from app.jwt import generate_token, validate_token


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.LargeBinary(60), nullable=False)
    address = db.Column(db.Text, nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(60), nullable=False)
    food_request = db.relationship('FoodRequest', backref='restaurant', lazy=True)
    rewards = db.relationship('Rewards', backref='restaurant', lazy=True)

    def __init__(self, **kwargs):
        super(Restaurant, self).__init__(**kwargs)

        self.email = self.email.strip()
        self.name = self.name.strip()
        self.password = bcrypt.hashpw(
            self.password.encode(), bcrypt.gensalt()
        )

    def __repr__(self):
        return f"<Restaurant id: {self.id} {self.email}>"

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
            "restaurant_id": self.id,
            "is_driver": False
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
            return Restaurant.query.get(user_identity)

        return Restaurant.query.filter(
            Restaurant.email.ilike(user_identity)
        ).first()
