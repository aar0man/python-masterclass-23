from django.contrib.auth.models import User
from graphene import Mutation, List, String, Int, ObjectType, JSONString, Field, Argument, InputObjectType, Boolean
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = User


class UserInfo(InputObjectType):
    username = String()
    email = String()


# Query
class UserInfoQuery(ObjectType):
    users_info_by_ids = Field(JSONString, ids=List(Int))

    def resolve_users_info_by_ids(self, info, ids=[]):
        # authorization not added but it should be based on JWT previous logic
        users = User.objects.filter(id__in=ids)
        return {int(user.id): {
            'username': user.username,
            'email': user.email
        } for user in users}


# Migrations

class UserUpdateMutation(Mutation):
    class Arguments:
        user_info = Argument(UserInfo)

    # The class attributes define the response of the mutation
    user = Field(UserType)

    def mutate(self, info, user_info, **kwargs):
        user_id = info.context.user.id
        user = User.objects.get(id=user_id)
        user.username = user_info.get('username')
        user.email = user_info.get('email')
        user.save()
        return UserUpdateMutation(user=user)
