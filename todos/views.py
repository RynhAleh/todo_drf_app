from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, People
from .serializers import TodoSerializer, PeopleSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('-created_at')
    serializer_class = TodoSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
# Create your views here.
