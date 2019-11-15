from django.db import models
from django.contrib.auth.models import User
from account.models import Account

class Expense_Type(models.Model):
    name = models.TextField(max_length=30)

class Expense(models.Model):
    name = models.TextField(max_length=40)
    price = models.IntegerField()
    expense_type = models.ForeignKey(Expense_Type, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, R$ {str(self.price)[:-2]},{str(self.price)[-2:]}'

