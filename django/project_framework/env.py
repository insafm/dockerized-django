import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

relative_path = "env/.env"
env_path = env.path('FILE', default=(environ.Path(__file__) - 4).path(relative_path)())()

# Take environment variables from .env file
env.read_env(os.path.join(env_path))