import graphene
from user.user_schema import UserInfoQuery, UserUpdateMutation


class UserQuery(UserInfoQuery):
   pass


class UserMutation(graphene.ObjectType):
   update_user_info = UserUpdateMutation.Field()
   pass