from rest_framework import serializers
from account.models import Account, Account_Type

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
