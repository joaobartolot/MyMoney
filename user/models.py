from django.db import models
from django.contrib.auth.models import User

from .expense import Expense

# Create your models here.

class User_Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
