from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'lname', 'email', 'image']
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre',}),
            'lname': forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file','placeholder':'Foto'}),
        }