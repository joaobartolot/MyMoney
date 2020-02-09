from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    """
    - endpoit:
        '/api/register'
    - parameters:
        username, password, first_name, last_name
    """

    model = User
    permission_classes = [ AllowAny ]
    serializer_class = UserSerializer
