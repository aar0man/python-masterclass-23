from rep_common.config import get_config, is_production, is_development

if is_production():
    ALLOWED_HOSTS = ['masterclass.assist.ro']
elif is_development():
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_sso.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': ('rep_common.authentication.permission_classes.PermissionClass',),
}

REST_FRAMEWORK_SSO = {
    'VERIFY_SESSION_TOKEN': False,
    'IDENTITY': 'app_server',
    'KEY_STORE_ROOT': 'rep_common/keys',
    'ACCEPTED_ISSUERS': ['users_microservice'],
    'PUBLIC_KEYS': {
        'auth_server': [get_config("AUTH_KEY_FILE_PATH")],  # only public keys in these files
    },
    'AUTHENTICATE_HEADER':'Bearer',
    'AUTHENTICATE_PAYLOAD': 'rep_common.authentication.authentication_service.authenticate_payload'
}
