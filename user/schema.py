from graphene import ObjectType,InputObjectType,Mutation, String, Field, Schema, ID, Int, List, NonNull, DateTime,Boolean
# from graphene_django.types import DjangoObjectType, ObjectType,
from .models import *


#types
class TodoType(ObjectType):
    id = ID()
    title = String()
    description = String()
    status=String()

class TodoInput(InputObjectType):
    title = String(required=True)
    description = String(required=True)
    status = Int(default_value=1)



#get
class TodoQuery(ObjectType):
    todo = Field(TodoType, id=Int())
    todos = List(TodoType)

    def resolve_todo(self, info, **kwargs):
        id = kwargs.get('id')
        try:
            todo = Todo.objects.get(pk=id)
        except:
            todo = None
        return todo

    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()

#post
class CreateTodo(Mutation):
    class Arguments:
        input = TodoInput(required=True)

    todo = Field(TodoType)

    def mutate(self, info, input):
        todo = Todo.objects.create(
            title=input.title,
            description=input.description,
            status=input.status
        )
        return CreateTodo(todo=todo)


#update
class UpdateTodo(Mutation):
    class Arguments:
        id = Int(required=True)
        input = TodoInput(required=True)

    todo = Field(TodoType)

    def mutate(self, info, id, input):
        todo = Todo.objects.get(pk=id)
        todo.title = input.title
        todo.description = input.description
        todo.status = input.status
        todo.save()
        return UpdateTodo(todo=todo)

class DeleteTodo(Mutation):
    class Arguments:
        id = Int(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            todo = Todo.objects.get(pk=id)
            todo.delete()
            ok = True
        except:
            ok = False
        return DeleteTodo(ok=ok)



class Mutation(ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()

   
schema = Schema(query=TodoQuery,mutation=Mutation)