import os

from envparse import env

basedir = os.path.abspath(os.path.dirname(__file__))

env.read_envfile()

ENABLED_MODULES = [

    "api" # This always has to be last
]

SQLALCHEMY_DATABASE_URI = env("DATABASE_URL", default="postgresql:///api")
