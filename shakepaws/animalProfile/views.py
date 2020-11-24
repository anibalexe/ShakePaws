from django.shortcuts import render, get_object_or_404
from shelter.models import Animal, Sponsor, Animal_sponsor
# Create your views here.
#def profile(request):
#    return render(request, "animalProfile/profile.html")

def profile(request, animal_id):
    sponsor = Sponsor.objects.all()
    animal_sponsor = Animal_sponsor.objects.all()
    animal = get_object_or_404(Animal, animal_id = animal_id)
    return render(request, "animalProfile/profile.html", {'animal':animal, 'sponsor':sponsor, 'animal_sponsor':animal_sponsor})

def validation(request, animal_id, sponsor_id):
    animal = get_object_or_404(Animal, animal_id = animal_id)
    sponsor = get_object_or_404(Sponsor, sponsor_id = sponsor_id)
    return render(request, "animalProfile/validation.html", {'animal':animal, 'sponsor':sponsor})
