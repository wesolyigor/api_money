from rest_framework import viewsets

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewsSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


'''
GET api/ ->
GET api/{id} -> detail

POST todos/ -> create
PUT todos/{id}/ -> update
PATCH todos/{id}/ -> partial update
DELETE todos/{id}/ -> delete

'''