from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators

from user.models import (SizeProductMapping, ColorProductMapping, PaperChoiceProductMapping,
                         ShrinkWrappingProductMapping, AqutousCoatingProductMapping, FoldingOptionsProductMapping,
                         NoOfMonthsProductMapping,
                         HoleDrillingProductMapping, BindingMethodProductMapping, ImageTemplateProductMapping, User,
                         Order, Packages, HoleDrilling)


class EditProfile(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput({'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput({'placeholder': 'Last Name'}), required=True)
    email = forms.EmailField(widget=forms.TextInput({'placeholder': 'Email'}), required=True,
                             validators=[validators.validate_email])
    avatar = forms.ImageField(required=False, validators=[validators.validate_image_file_extension])
    username = forms.CharField(widget=forms.TextInput({'placeholder': 'User Name', 'value': ' '}), required=True)

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'gender']


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


class HoleDrillingForm(forms.ModelForm):
    class Meta:
        model = HoleDrilling
        fields = ['hole']


class BindingMethodProductMapForm(forms.ModelForm):
    class Meta:
        model = BindingMethodProductMapping
        fields = ['binding_method_id', 'prod_id']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'avatar', 'email', 'password1', 'password2', 'gender', 'role']


class EditUserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'gender', 'role')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = ['package_Name', 'attribute_values', 'package_Price', 'prod_ID']
