from django.urls import path

from .views import home_view, account_list

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts', account_list, name='account-list')
]
