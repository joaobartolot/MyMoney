from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        fields = '__all__'