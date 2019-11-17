from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView

from .forms import UserCreateForm

class UserRegistrationView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = ''

    template_name = 'user/register.html'
