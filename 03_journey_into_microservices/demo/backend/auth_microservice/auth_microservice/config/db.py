from rep_common.config import get_config, add_db_prefix

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': get_config('DEFAULT_DB_USERNAME', default='masterclass'),
        'PASSWORD': get_config('DEFAULT_DB_PASSWORD', default='masterclass'),
        'NAME': get_config('DEFAULT_DB_NAME', default=add_db_prefix(suffix='auth')),
        'HOST': get_config('DEFAULT_DB_HOST', default='mysql'),
        'PORT': get_config('DEFAULT_DB_PORT', default='3306'),
    }
}
