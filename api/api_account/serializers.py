from rest_framework import serializers
from account.models import Account, Account_Type

class AccountSerializer(serializers.ModelSerializer):
    cardImg = serializers.CharField(source='getCardImg')
    class Meta:
        model = Account
        fields = '__all__'
