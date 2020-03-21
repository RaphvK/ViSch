from django.contrib.auth.models import User
from django.db import models
import os
#from django.contri.auth.models import User

class Ort(models.Model):
    name = models.CharField(max_length=50)
    plz = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Adresse(models.Model):
    strasse = models.CharField(max_length=40)
    #gpsDaten

class Inhaber(models.Model):
    inhaberName = models.CharField(max_length=40)
    phone = models.PositiveIntegerField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)
    mail = models.EmailField(blank=True)

class Shop(models.Model):
    shopType = models.TextChoices('shopType', 'Restaurant Bekleidungsgeschäft Gärtnerei Uhrenmacher Juwelier Buchladen Handwerk Parfümerie Optiker Entertainment')
    name = models.CharField(max_length=40)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=70, choices=shopType.choices)
    shortInfo = models.CharField(max_length=200)
    #pics = models.
    delievery = models.BooleanField(default=False)
    inhaber = models.ForeignKey(Inhaber, on_delete=models.CASCADE, blank=True, null=True)

    # chatEnable = models.BooleanField(default=True)
    #chat
   # def save(self, *args, **kwargs):
   #     super().save(*args,**kwargs)
    def __str__(self):
        return self.name

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Ware(models.Model):
    laden = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    titel = models.CharField(max_length=30)
    info = models.CharField(max_length=200)
    preis = models.DecimalField(max_digits=4, decimal_places=2)



#class Chat(models.Model):
    #name1
    #name2
    #timestamp
