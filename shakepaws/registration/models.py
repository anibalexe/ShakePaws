from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length = 50, verbose_name = "Nombre")
    lname = models.CharField(max_length = 50, verbose_name = "Apellido")
    email = models.EmailField(verbose_name = "E-mail")

    class Meta:
        ordering = ['user__username']