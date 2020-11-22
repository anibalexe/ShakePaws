from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import SponsorProfileForm
# Create your views here.
#def profile(request):
#    return render(request, "animalProfile/profile.html")

def profile(request, id):
    user = get_object_or_404(User, id = id)
    return render(request, "sponsorProfile/profile.html", {'user':user})

class SponsorProfileUpdate(UpdateView):
    model = User
    form_class = SponsorProfileForm
    template_name_suffix = "_update_form"

   # def get_success_url(self):
    #    return reverse_lazy('users:update', args=[self.object.id])