from django.urls import path
from .api_account.views import AccountCreateView, AccountUserList
from .api_user.views import RegistrationView

urlpatterns = [
    path('account-create/', AccountCreateView.as_view()),
    path('account-user-list/', AccountUserList.as_view()),
    path('user-create/', RegistrationView.as_view()),
]
