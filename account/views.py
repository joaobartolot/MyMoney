from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account

@login_required(login_url='login/')
def home_view(request):
    context = {
        'title': 'Home',
    }

    return render(request, template_name='account/home.html', context=context)

def account_list(request):
    context = {
        'title': 'Accounts'
    }

    return render(request, template_name='account/account_list.html', context=context)
