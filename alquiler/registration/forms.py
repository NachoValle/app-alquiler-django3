from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
         model = Profile
         fields = ['avatar_user','movil',]
         widgets = {
                 'avatar_user': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
                 'movil':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Telefono'}),
                 
        
         }

class EmailForm(forms.ModelForm):
        email= forms.EmailField(required=True, help_text="Requerido, debe ser valido. Para poder recuperar la contraseña")
        class Meta:
                model = User
                fields = ['email']
        
        def clean_email(self):
                email = self.cleaned_data.get('email')
                if 'email' in self.changed_data:
                      
                        return email

class UsuariosForm(forms.ModelForm):
        class Meta:
         model = Profile
         fields = ['madrid','valladolid','salamanca','las_palmas','mallorca','zamora','todas','p_vehiculos','p_user']
         
        
                
                