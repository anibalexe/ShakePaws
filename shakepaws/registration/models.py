from django.db import models
from django.contrib.auth.models import User
from shelter.models import Animal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name = "Imagen", upload_to = "Perfiles", null=True, blank=True)
    fname = models.CharField(max_length = 50, verbose_name = "Nombre")
    lname = models.CharField(max_length = 50, verbose_name = "Apellido")
    email = models.EmailField(verbose_name = "E-mail")
    phone = models.CharField(max_length = 50, verbose_name = "Celular", blank=True)
    address = models.CharField(max_length = 50, verbose_name = "Direccion", blank=True)
    role = models.CharField(max_length = 50, verbose_name = "Cargo", blank=True)
    sponsorsToAnimals = models.ManyToManyField(Animal, through = "Profile_animal" , verbose_name = "ApadrinamientosAAnimales")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__username']

    def __str__(self):
        return self.fname

    

class Profile_animal(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    sponsor = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")

    class Meta:
        verbose_name = "Apadrinamiento de usuario"
        verbose_name_plural = "Apadrinamientos de usuarios"
        ordering = ["-created"]
