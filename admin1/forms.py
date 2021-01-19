from django import forms

from user.models import SizeProductMapping


class SizeProductMapForm(forms.ModelForm):

    class Meta:
        model = SizeProductMapping
        fields = ['size_id', 'prod_id']
