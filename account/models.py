from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account_Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Account Type'
        db_table = 'account_type'

class Bank(models.Model):
    name = models.CharField(max_length=20)
    rate = models.FloatField(null=True)
    income = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Bank'
        db_table = 'bank'

class Account(models.Model):
    name = models.CharField(max_length=20)
    balance = models.IntegerField()
    initial_balance = models.IntegerField()
    salary = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_type = models.ForeignKey(Account_Type, on_delete=models.CASCADE)

    @property
    def getCardImg(self):
        cardImg = self.bank.name + '.png'

        return cardImg

    def __str__(self):
        return f'{self.name}({self.balance}), user: {self.user}'

    class Meta:
        verbose_name = 'Account'
        db_table = 'account'
