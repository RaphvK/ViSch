from django.contrib.auth.models import User
from django.db import models
import os


def get_image_path(instance, filename):
   return os.path.join('photos', str(instance.id), filename)


class Ort(models.Model):
    name = models.CharField(max_length=50)
    plz = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Adresse(models.Model):
    strasse = models.CharField(max_length=40)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Owner(models.Model):
    ownerName = models.CharField(max_length=40)
    phone = models.PositiveIntegerField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)
    mail = models.EmailField(blank=True)


class Shop(models.Model):
    shopType = models.TextChoices('shopType',
                                  'Restaurant Bekleidungsgeschäft Gärtnerei Uhrenmacher Juwelier Buchladen Handwerk Parfümerie Optiker Entertainment')
    name = models.CharField(max_length=40)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=70, choices=shopType.choices)
    shortInfo = models.CharField(max_length=200)
    pics = [models.ImageField(upload_to=get_image_path, blank=True, null=True)]
    delieverys = models.BooleanField(default=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
    chatEnable = models.BooleanField(default=False)

    # chat
    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
    def __str__(self):
        return self.name

    def addPic(self):
        if len(Shop.pics) >= 10:
            return 'Bereits maximale Anzahl an Bildern erreicht.'
        filename = str(Shop.id)+str(Shop.name)+str(len(Shop.pics))   #Todo: sinnvolle Namensverwaltung nicht überscheiben von bereits vorhandenen
        Shop.pics.append(models.ImageField(upload_to=get_image_path(self, filename), name=filename))
        return 'Bild hochgeladen.'

    def deletePic(self, filename):
        try:
            Shop.pics.remove(models.ImageField(name=filename))
        except ValueError:
            return 'Bild nicht gefunden.'
        return 'Bild gelöscht.'

    def articleAdd(self, articletitle, articleprice):
        article1 = Article(shop=self.id, titel=articeltitle, price=articelprice)


    def articelDelete(self, articletitle):
        article = Article.objects.filter(shop=self.id)
        if article is None:
            return
        del article


class Delievery(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    shipping_costs = models.DecimalField(max_digits=3, decimal_places=2)
    sum_of_prices = models.DecimalField(max_digits=7, decimal_places=2)


class Article(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    delivery = models.ManyToManyField(Delievery)
    pics = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    titel = models.CharField(max_length=30)
    info = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    units = models.PositiveSmallIntegerField()

    def addPhoto(self, filename):
        filename = str(self.id) + str(self.name)
        Article.pics.append(models.ImageField(upload_to=get_image_path(self, filename), name=filename))
        return 'Bild hochgeladen.'

    def deletePic(self, filename):
        try:
            Article.pics.remove(models.ImageField(name=filename))
        except ValueError:
            return 'Bild nicht gefunden.'
        return 'Bild gelöscht.'


# class Chat(models.Model):
# name1
# name2
# timestamp
