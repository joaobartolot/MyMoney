from django.contrib import admin

from .models import Account, Account_Type, Bank

admin.site.register(Account)
admin.site.register(Account_Type)
admin.site.register(Bank)
