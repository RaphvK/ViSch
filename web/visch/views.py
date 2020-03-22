from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse
from .forms import AddressForm
from .models import Shop, Adresse


def index(request):
    address_form = AddressForm()
    # if this is a POST request we need to process the form data

    return render(request, 'visch/index.html',
                  {'address_form': address_form})


def map_view(request):
    map_center = {'lon': 0, 'lat': 0}
    address_string = "Address not found!"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.get_lonlat_from_address()
            map_center['lon'] = new_address.longitude
            map_center['lat'] = new_address.latitude
            address_string = new_address.strasse + ", " + new_address.plz + " " + new_address.ort

            Shop.objects.all().delete()
            test_address = Adresse(strasse="Wupperstr. 5", plz="40219", ort="Düsseldorf")
            test_address.get_lonlat_from_address()
            test_address.save()
            Shop.objects.create(name="Laden", shortInfo="Super Restaurant!", adresse=test_address)

            shops = Shop.objects.all()

            mapbox_access_token = 'pk.eyJ1IjoicmFmZml2ayIsImEiOiJjazgyeGdiajIxMmFuM2xydWRxMjc1OWo1In0.ScA_dn1wK1jJ2WEC7xIegA'


            return render(request, 'visch/map.html',
                          {'mapbox_access_token': mapbox_access_token,
                           'lon': map_center['lon'],
                           'lat': map_center['lat'],
                           'address_string': address_string,
                           'shops': shops})
        return render(request, 'visch/index.html')


def register_view(request):
    register_form = UserCreationForm()
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'visch/register.html', {'register_form': register_form})

def login_view(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'visch/login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect(reverse('visch:index'))

def betreiber_view(request):
    return render(request, 'visch/betreiber.html')