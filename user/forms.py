from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'ng-model': 'username'})
        self.fields['password1'].widget.attrs.update({'ng-model': 'password'})
        self.fields['password2'].widget.attrs.update({'ng-model': 'password_confirmation'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']