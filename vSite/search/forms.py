from django import forms


class SearchProfileForm(forms.ModelForm):
    looking_for = forms.CharField()
    age_min = forms.IntegerField()
    age_max = forms.IntegerField()
    city = forms.CharField()

    class Meta:
        fields = (
            'looking_for',
            'age_min',
            'age_max',
            'city',
        )
