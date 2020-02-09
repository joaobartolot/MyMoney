from django.urls import path
from .api_account.views import AccountCreateView, AccountUserList
from .api_user.views import CreateUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token-auth/', obtain_auth_token, name='token-auth'),

    path('account-create/', AccountCreateView.as_view()),
    path('account-user-list/', AccountUserList.as_view()),

    path('register/', CreateUserView.as_view()),
]
