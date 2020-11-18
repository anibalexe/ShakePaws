from django.shortcuts import render, get_object_or_404
from shelter.models import Animal
# Create your views here.
#def profile(request):
#    return render(request, "animalProfile/profile.html")

def profile(request, animal_id):
    animal = get_object_or_404(Animal, animal_id = animal_id)
    return render(request, "animalProfile/profile.html", {'animal':animal})
