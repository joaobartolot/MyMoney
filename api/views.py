from django.shortcuts import render
from .serializers import AccountSerializer
from rest_framework.generics import CreateAPIView
from account.models import Account

class AccountCreateView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
