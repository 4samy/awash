import settings

import bcrypt
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=True)
    password = db.Column(db.LargeBinary(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    car_description = db.Column(db.Text(), nullable=True, default=None)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        self.email = self.email.strip()
        self.first_name = self.first_name.strip()
        self.password = bcrypt.hashpw(
            self.password.encode(), bcrypt.gensalt()
        )

    def verify_password(self, password):
        """Returns True if this password matches for this User."""

        if isinstance(password, str):
            password = password.encode()

        if bcrypt.checkpw(password, self.password):
            return True

        return False





