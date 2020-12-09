from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
from django.shortcuts import render
from .forms import ProfileForm
from registration.models import Profile_animal
from shelter.models import Animal, Sponsor
# Create your views here.

from django.contrib.auth.decorators import user_passes_test

def staff_check(user):
    return user.is_staff

def panel(request):
    return render(request, "registration/panel.html")

def notification(request):
    animal = Animal.objects.all()
    sponsor = Sponsor.objects.all()
    profile_animal = Profile_animal.objects.all()
    return render(request, "registration/notification.html", {'animals':animal, 'sponsors':sponsor, 'profile_animals':profile_animal})

def sponsors(request):
    animal = Animal.objects.all()
    sponsor = Sponsor.objects.all()
    profile_animal = Profile_animal.objects.all()
    return render(request, "registration/sponsors.html", {'animals':animal, 'sponsors':sponsor, 'profile_animals':profile_animal})


def profile(request):
    profile_animal = Profile_animal.objects.all() 
    return render(request, "registration/profile.html", {'profile_animal':profile_animal})

def perfil(request):
    perfil = Profile.objects.all()
    return render(request, "registration/profileAdmin.html", {'perfiles':perfil})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Repite la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse_lazy('perfil-padrino') + '?ok'


    def get_object(self):
        # recuperar el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

