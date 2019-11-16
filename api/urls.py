from django.urls import path
from .views import AccountCreateView

urlpatterns = [
    path('account-create/', AccountCreateView.as_view()),
]
