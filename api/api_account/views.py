from django.shortcuts import render
from .serializers import AccountSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from account.models import Account

class AccountCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
