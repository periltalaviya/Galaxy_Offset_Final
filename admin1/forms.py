from django import forms

from user.models import SizeProductMapping, ColorProductMapping, PaperChoiceProductMapping, \
    ShrinkWrappingProductMapping, AqutousCoatingProductMapping, FoldingOptionsProductMapping, NoOfMonthsProductMapping, \
    HoleDrillingProductMapping, BindingMethodProductMapping, ImageTemplateProductMapping


class SizeProductMapForm(forms.ModelForm):
    class Meta:
        model = SizeProductMapping
        fields = ['size_id', 'prod_id']

class ImageTempProductMapForm(forms.ModelForm):
    class Meta:
        model = ImageTemplateProductMapping
        fields = ['temp_id', 'prod_id']

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


class FoldingOptionProductMapForm(forms.ModelForm):
    class Meta:
        model = FoldingOptionsProductMapping
        fields = ['folding_options_id', 'prod_id']


class NoOfMonthsProductMapForm(forms.ModelForm):
    class Meta:
        model = NoOfMonthsProductMapping
        fields = ['no_of_months_id', 'prod_id']


class HoleDrillingProductMapForm(forms.ModelForm):
    class Meta:
        model = HoleDrillingProductMapping
        fields = ['hole_drilling_id', 'prod_id']

class BindingMethodProductMapForm(forms.ModelForm):
    class Meta:
        model = BindingMethodProductMapping
        fields = ['binding_method_id', 'prod_id']
