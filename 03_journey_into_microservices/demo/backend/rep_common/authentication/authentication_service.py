
from django.contrib.auth.models import User

from rep_common.config import get_config
from rest_framework_sso import claims

APP_USER_GROUP = 'app_user'

def create_authorization_payload(session_token, user, **kwargs):
    return {
        claims.TOKEN: claims.TOKEN_AUTHORIZATION,
        claims.SESSION_ID: session_token.pk,
        claims.USER_ID: user.pk,
        claims.EMAIL: user.email,
        claims.ISSUER: "auth_microservice",
    }


def authenticate_payload(payload, request):
    user_id = payload.get(claims.USER_ID)
    username = payload.get('username')
    user_first_name = payload.get('userFirstName')
    user_last_name = payload.get('userLastName')
    user_email = payload.get(claims.EMAIL)

    user = User(id=user_id, username=username, first_name=user_first_name, last_name=user_last_name, email=user_email)
    user.permissions = payload.get('permissions')
    return user


def handle_headers(headers=None):
    # Adding api key to headers for requests 
    if headers is None:
        headers = {}
    
    # remote api key enables using with service of other environment
    if get_config("REMOTE_API_KEY") is not None:
        api_key = get_config("REMOTE_API_KEY")
    else:
        api_key = get_config("API_KEY")
    
    headers["API-KEY"] = api_key
    return headers
