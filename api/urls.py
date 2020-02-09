from django.urls import path
from .api_account.views import AccountCreateView, AccountUserList
from django.conf.urls import url
from .api_user.views import CreateUserView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My Money API')

urlpatterns = [
    url(r'^$', schema_view),

    path('token-auth/', obtain_auth_token, name='token-auth'),

    path('account-create/', AccountCreateView.as_view()),
    path('account-user-list/', AccountUserList.as_view()),

    path('register/', CreateUserView.as_view()),
]
