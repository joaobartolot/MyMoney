from django.contrib import admin

from .models import Expense, Expense_Type

admin.site.register(Expense)
admin.site.register(Expense_Type)
