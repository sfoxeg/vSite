from django import forms
from user.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'goal',
            'first_name',
            'last_name',
            'description',
            'city',
            'height',
            'weight',
        )
