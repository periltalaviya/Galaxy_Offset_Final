from django import forms

from user.models import SizeProductMapping, ColorProductMapping, PaperChoiceProductMapping, \
    ShrinkWrappingProductMapping, AqutousCoatingProductMapping


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


class ShrinkWrappingProductMapForm(forms.ModelForm):
    class Meta:
        model = ShrinkWrappingProductMapping
        fields = ['shrink_wrapping_id', 'prod_id']


class AqutousCoatingProductMapForm(forms.ModelForm):
    class Meta:
        model = AqutousCoatingProductMapping
        fields = ['aqutous_coating_id', 'prod_id']