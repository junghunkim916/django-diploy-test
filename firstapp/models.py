from django.db import models

# Create your models here.

class User(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length = 200)
    age = models.IntegerField()
    photo = models.ImageField(blank = True, upload_to = "")
