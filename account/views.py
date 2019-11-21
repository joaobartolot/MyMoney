from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account

@login_required(login_url='login/')
def home_view(request):
    context = {
        'title': 'Home',
        'accounts': Account.objects.all().filter(user=request.user.id)
    }

    return render(request, template_name='account/home.html', context=context)
