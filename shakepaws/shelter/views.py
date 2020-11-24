from django.shortcuts import render
from .models import Animal, Sponsor, Animal_sponsor

def sponsoring(request):
    animals = Animal.objects.all()
    sponsors = Sponsor.objects.all()
    animal_sponsor = Animal_sponsor.objects.all()
    return render(request, "shelter/sponsoring.html", {"sponsors": sponsors, "animals": animals, "animal_sponsor":animal_sponsor})


# Create your views here.
