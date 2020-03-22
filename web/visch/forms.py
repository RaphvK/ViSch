from django import forms


class AddressForm(forms.Form):
    street = forms.CharField(label='Straße', max_length=200)
    town = forms.CharField(label='Ort', max_length=200)
