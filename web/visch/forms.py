from django import forms
from .models import Address
from .models import Shop

class AddressForm(forms.ModelForm):
     class Meta:
         model = Address
         exclude = ['latitude', 'longitude']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ['pics', 'owner', 'shortInfo']

