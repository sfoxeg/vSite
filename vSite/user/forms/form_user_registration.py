from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    date_of_birth = forms.CharField()
    sex = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'sex'
        )
