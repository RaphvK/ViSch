from django.contrib.auth.models import User
from django.db import models
#from django.contri.auth.models import User

# Create your models here.
from django.utils import timezone


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)