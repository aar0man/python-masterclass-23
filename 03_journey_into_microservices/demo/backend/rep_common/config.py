import os
from decouple import config

from rep_common.enums import Environment

DEFAULT_PASSWORD = 'masterclass'


def is_beat():
    return get_config('IS_BEAT') == 'True'


def add_db_prefix(suffix):
    return f"masterclass_{suffix}"


def get_environment() -> str:
    return config('ENVIRONMENT', default=Environment.DEVELOPMENT.value)



def is_production():
    return get_environment() == Environment.PRODUCTION.value


def is_development():
    return get_environment() == Environment.DEVELOPMENT.value


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
        return DEFAULT_PASSWORD

    elif config_name == 'AUTH_KEY_PUBLIC_FILE_PATH':
        if is_production():
            return 'public.key.prod.pem'
        return 'public.key.dev.pem'

    elif config_name == 'AUTH_KEY_PRIVATE_FILE_PATH':
        if is_production():
            return 'private.keys.prod.pem'
        return 'private.key.dev.pem'

    if default:
        return config(config_name, default=default)

    return None
