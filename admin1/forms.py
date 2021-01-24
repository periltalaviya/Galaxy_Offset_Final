from django import forms

from user.models import SizeProductMapping, ColorProductMapping, PaperChoiceProductMapping


class SizeProductMapForm(forms.ModelForm):

    class Meta:
        model = SizeProductMapping
        fields = ['size_id', 'prod_id']


class ColorProductMapForm(forms.ModelForm):

    class Meta:
        model = ColorProductMapping
        fields = ['color_id', 'prod_id']


class PaperProductMapForm(forms.ModelForm):

    class Meta:
        model = PaperChoiceProductMapping
        fields = ['paper_id', 'prod_id']
