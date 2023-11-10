from rest_framework_sso.authentication import JWTAuthentication
from graphene_django.views import GraphQLView
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.request import Request
from rest_framework.settings import api_settings


class JWTGraphQLView(JWTAuthentication, GraphQLView):

    def parse_body(self, request):
        if isinstance(request, Request):
            return request.data
        return super(JWTGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(JWTGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes(api_settings.DEFAULT_PERMISSION_CLASSES)(view)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = api_view(['GET', 'POST'])(view)
        return view
        