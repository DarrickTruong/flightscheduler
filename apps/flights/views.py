from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
