from email.policy import default
from django.contrib.auth.models import User
from graphene import ObjectType, String, Field, Schema, ID, Int, List, NonNull, DateTime

class Query(ObjectType):
    userName = String(first_name=String(default_value="Hello"), last_name=String(default_value="World"))
    userAge = Int(age=Int(default_value=0))

    def resolve_userName(self, info, first_name, last_name):
        return f'{first_name} {last_name}'

    def resolve_userAge(self, info, age):
        return age

schema = Schema(query=Query)


