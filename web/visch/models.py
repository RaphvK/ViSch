from django.db import models
#from django.contri.auth.models import User

class Ort(models.Model):
    name = models.CharField(max_length=50)
    plz = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name
class Adresse(models.Model):
    strasse = models.CharField(max_length=40)
    #ort
    #gpsDaten

class Inhaber(models.Model):
    inhaberName = models.CharField(max_length=40)
    phone = models.PositiveIntegerField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)
    mail = models.EmailField(blank=True)

class Laden(models.Model):
    #KATEGORIE_IN_CHOICES = [
     #   (Restaurant, ('Restaurant', 'Gaststätte', 'Wirtshaus', 'Take-Away')),
      #  (KLEIDUNG, 'Kleidung'),
      #  (DEFAULT, 'Sonstige'),
    #]
    name = models.CharField(max_length=40)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=70) #, choices=KATEGORIE_IN_CHOICES, default='DEFAULT')
    #shortInfo
    #pics = models.
    #chatEnable = models.BooleanField(default=True)
    delievery = models.BooleanField(default=False)
    inhaber = models.ForeignKey(Inhaber, on_delete=models.CASCADE, blank=True, null=True)

    #chat
   # def save(self, *args, **kwargs):
   #     super().save(*args,**kwargs)
    def __str__(self):
        return self.name

class Ware(models.Model):
    laden = models.ForeignKey(Laden, on_delete=models.DO_NOTHING)
    #photo
    #titel
    #beschreibung
    #preis



#class Chat(models.Model):
    #name1
    #name2
    #timestamp
