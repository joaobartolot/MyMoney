from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account_Type(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Bank(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Account(models.Model):
    name = models.TextField(max_length=20)
    balance = models.IntegerField()
    initial_balance = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(Account_Type, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.balance}), user: {self.user}'
