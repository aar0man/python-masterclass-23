from django.conf.urls import url
from django.urls import path, include
from rest_framework_sso.views import obtain_session_token, obtain_authorization_token

from rep_common.authentication.jwt_graphql_view import JWTGraphQLView
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^session/', obtain_session_token),
    url(r'^authorize/', obtain_authorization_token),

    path('graphql/', JWTGraphQLView.as_view()),

]