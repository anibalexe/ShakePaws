from django.db import models
from django.contrib.auth.models import User
from shelter.models import Animal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length = 50, verbose_name = "Nombre")
    lname = models.CharField(max_length = 50, verbose_name = "Apellido")
    email = models.EmailField(verbose_name = "E-mail")
    sponsorsToAnimals = models.ManyToManyField(Animal, through = "Profile_animal" , verbose_name = "ApadrinamientosAAnimales")

    class Meta:
        ordering = ['user__username']

    

class Profile_animal(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    sponsor = models.IntegerField()