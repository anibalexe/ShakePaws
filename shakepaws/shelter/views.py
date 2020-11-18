from django.shortcuts import render
from .models import Animal, Sponsor

def sponsoring(request):
    animals = Animal.objects.all()
    sponsors = Sponsor.objects.all()
    return render(request, "shelter/sponsoring.html", {"sponsors": sponsors, "animals": animals})


# Create your views here.
