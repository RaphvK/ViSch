from django import forms
from .models import Adresse


class AddressForm(forms.ModelForm):
     class Meta:
         model = Adresse
         exclude = ['latitude', 'longitude']
