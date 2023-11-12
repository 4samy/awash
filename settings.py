import os

from envparse import env

basedir = os.path.abspath(os.path.dirname(__file__))

env.read_envfile()

DEBUG = env("DEBUG", default="no", cast=bool)
SECRET_KEY = env("SECRET_KEY", default="secret_key")

# JWT signature configuration ***Salt is always required***
TOKEN_TYPES = {
    "session": {
        "expires_in": 15552000,
        "salt": "session"
    }
}


ENABLED_MODULES = [
    "auth",
    "driver",
    "restaurant",
    "food_request",
    "rewards",
    "test",

    "api"  # This always has to be last
]

SQLALCHEMY_DATABASE_URI = env("DATABASE_URL", default="postgresql:///DonateFood-API")
SQLALCHEMY_TRACK_MODIFICATIONS = False


