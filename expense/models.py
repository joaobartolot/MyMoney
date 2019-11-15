from django.db import models
# from .user import User_Expense

# Create your models here.

class Expense_Type(models.Model):
    name = models.TextField(max_length=30)

class Expense(models.Model):
    name = models.TextField(max_length=40)
    price = models.IntegerField()
    expense_type = models.ForeignKey(Expense_Type, on_delete=models.CASCADE)
    # user_expense = models.ForeignKey(User_Expense, on_delete=models.CASCADE)
    # account = models.ForeignKey(Account, on_delete=models.CASCADE)

