"""
This module defines environment variables for the Django application.
It is intended to store sensitive information like database credentials
and API keys as environment variables, rather than hard-coding them in the application code.

To use these variables, import this module and access them as properties of the `environ` object.
For example:

    from .env import env

    DATABASE_URL = env.get('DATABASE_URL')
    API_KEY = env.get('API_KEY')
"""

import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    APPLICATION_ID=(str, os.environ.get('APPLICATION_ID'))
)

RELATIVE_PATH = "env/.env"

# Change .env file according to APPLICATION_ID set in environment variable.
if env('APPLICATION_ID'):
    RELATIVE_PATH = "env/.env_" + env('APPLICATION_ID')

env_path = env.path('FILE', default=(environ.Path(__file__) - 3).path(RELATIVE_PATH)())()

# Take environment variables from .env file
env.read_env(os.path.join(env_path))
