from django.db import models

# Create your models here.    
class Sponsor(models.Model):
    sponsor_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    cost = models.IntegerField()

class Animal(models.Model):
    animal_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    lifestage = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add = True)
    Updated = models.DateTimeField(auto_now = True)
    sponsor = models.ForeignKey(Sponsor, on_delete = models.CASCADE)

#class Animal_sponsor(models.Model):
    #animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    #sponsor = models.ForeignKey(Sponsor, on_delete = models.CASCADE)