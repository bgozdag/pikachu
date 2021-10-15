from django import forms
from .models import Barista, Coffee


class BaristaForm(forms.ModelForm):
    class Meta:
        model = Barista
        fields = ['name', 'profile_pic', 'mail']
