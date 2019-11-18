from django.shortcuts import render
from .serializers import AccountSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from account.models import Account

class AccountCreateView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated]

class AccountUserList(ListAPIView):
    serializer_class = AccountSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = []

    def get_queryset(self):
        queryset = Account.objects.all().filter(user=self.request.user.id)
        return queryset
