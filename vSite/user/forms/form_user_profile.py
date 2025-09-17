from django import forms
from main.models import City
from user.models import UserProfile


class UserProfileForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    acting = forms.BooleanField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    description = forms.CharField()
    height = forms.CharField()
    weight = forms.CharField()

    class Meta:
        model = UserProfile
        fields = (
            'acting',
            'first_name',
            'last_name',
            'description',
            'city',
            'height',
            'weight',
        )
