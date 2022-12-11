from django.forms import ModelForm
from django import forms
from .models import Duck, Color, Owner

class DuckForm(ModelForm):
    class Meta:
        model = Duck
        fields = ['duck_image', 'duck_first_name', 'duck_last_name', 'duck_birthday', 'body_color', 'beak_color', 'Owner']

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['color_name']

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['owner_first_name', 'owner_last_name']
