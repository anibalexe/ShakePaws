from django import forms
from registration.models import Profile_animal

class Profile_animalForm(forms.ModelForm):
    class Meta:
        model = Profile_animal
        fields = ['profile', 'animal', 'sponsor']
        widgets = {
            'profile': forms.TextInput(attrs={'class':'form-control','placeholder':'Perfil', 'value':'1', 'type':'hidden'}),
            'animal': forms.TextInput(attrs={'class':'form-control','placeholder':'Animal',  'value':'123456', 'type':'hidden'}),
            'sponsor': forms.TextInput(attrs={'class':'form-control','placeholder':'Apadrinamiento', 'value':'123456', 'type':'hidden'}),
        }