from django import forms
from user.models import Climbing


class UserProfileClimbingForm(forms.ModelForm):
    class Meta:
        model = Climbing
        fields = (
            'leading',
            'where_leading',
            'bouldering',
            'where_bouldering',
            'speed',
            'alpinism',
            'belay',
            'belay_description',
        )
