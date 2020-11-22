from django import forms
#from .models import User
from django.contrib.auth.models import User

class SponsorProfileForm(forms.ModelForm):

    class meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
