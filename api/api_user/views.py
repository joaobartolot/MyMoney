from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from django.contrib.auth.models import User
from .serializers import RegistrationSerializer

class RegistrationView(CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
