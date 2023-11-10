from rep_common.config import get_config, is_production, is_development

if is_production():
    ALLOWED_HOSTS = ['masterclass.assist.ro']
elif is_development():
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']


CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SECURE = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_sso.authentication.JWTAuthentication',
    ),
}

REST_FRAMEWORK_SSO = {
    'IDENTITY': 'auth_microservice',
    'KEY_STORE_ROOT': 'rep_common/keys',
    'PUBLIC_KEYS': {
        'auth_microservice': [get_config("AUTH_KEY_PUBLIC_FILE_PATH")],
    },
    'PRIVATE_KEYS': {
        'auth_microservice': [get_config("AUTH_KEY_PRIVATE_FILE_PATH")],
    },
    'CREATE_AUTHORIZATION_PAYLOAD': 'rep_common.authentication.authentication_service.create_authorization_payload',

}