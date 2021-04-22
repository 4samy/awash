import os

from envparse import env

basedir = os.path.abspath(os.path.dirname(__file__))

env.read_envfile()

DEBUG = env("DEBUG", default="no", cast=bool)

ENABLED_MODULES = [
    "test",

    "api" # This always has to be last
]

SQLALCHEMY_DATABASE_URI = env("DATABASE_URL", default="postgresql:///api")
SQLALCHEMY_TRACK_MODIFICATIONS = False


