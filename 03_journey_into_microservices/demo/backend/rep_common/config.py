import os
from decouple import config

from rep_common.enums import Environment

DEFAULT_PSWD = 'masterclass'

def is_beat():
    return get_config('IS_BEAT') == 'True'


def add_db_prefix(suffix):
    return f"masterclass_{suffix}"

def get_environment() -> str:
    # docker in kubernetes receive the environment from deployments env vars and not the .env file
    env = os.getenv('ENVIRONMENT')
    if env is not None:
        # removing the pomi- from the env
        env = env.replace('pomi-', '')
    else:
        env = config('ENVIRONMENT', default=Environment.DEVELOPMENT.value)
    return str(env).lower()

def is_development():
    return os.getenv('ENVIRONMENT') == Environment.DEVELOPMENT.value



def is_production():
    return os.getenv('ENVIRONMENT') == Environment.PRODUCTION.value

def get_config(config_name: str, default=None, cast=None):
    if config_name == 'DEBUG':
        debug = os.getenv(config_name)
        if debug is not None:
            return debug == 'True'
        return config('DEBUG', default=True, cast=bool)

    if config_name == 'IS_BEAT':
        is_beat_value = os.getenv(config_name)
        if is_beat_value is not None:
            return is_beat_value
        return config('IS_BEAT', default='True')


    elif config_name == 'DEFAULT_DB_PASSWORD':
        if is_production():
            return config('PROD_DB_PASSWORD')
        elif is_development():
            return config('DEV_DB_PASSWORD')
        return DEFAULT_PSWD

    # Authentication keys file name
    elif config_name == 'AUTH_KEY_FILE_PATH':
        if is_production():
            return 'keys.prod.pem'
        elif is_development():
            return 'keys.dev.pem'
        return 'keys.pem'
