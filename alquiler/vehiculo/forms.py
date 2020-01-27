from django import forms

from .models import Vehiculo

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields=['activo','ciudad','tipo','placa','marca','modelo','combustible','color','bastidor','fecha_matricula','itv','image','odo',]
        widgets={
           'activo':forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'activar vehículo'}),
            'ciudad':forms.Select(attrs={'class':'form-control', 'placeholder':'Elige ciudad'}),
            'tipo':forms.Select(attrs={'class':'form-control',}),
            'placa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Matrícula'}),
            'marca':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
            'modelo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
            'combustible':forms.Select(attrs={'class':'form-control'}),
            'color':forms.Select(attrs={'class':'form-control'}),
            'bastidor':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bastidor'}),
            'fecha_matricula':forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'itv':forms.DateInput(attrs={'type': 'date','class':'form-control'}),

            'odo':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Odometro'}),

        }
        labels={
            
        }
    def clean_placa(self):
        placa = self.cleaned_data.get('placa')
        placa = placa.upper()
        if  Vehiculo.objects.filter(placa=placa).exists():
            raise forms.ValidationError("La matricula ya está registrada")
        return placa    
         
        
       




class VehiculoActualizarForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields=['activo','ciudad','tipo','marca','modelo','combustible','color','bastidor','fecha_matricula','itv','image','odo',]
        widgets={
           'activo':forms.CheckboxInput(attrs={'class':'form-control'}),
            'ciudad':forms.Select(attrs={'class':'form-control'}),
            'tipo':forms.Select(attrs={'class':'form-control'}),
            
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'modelo':forms.TextInput(attrs={'class':'form-control'}),
            'combustible':forms.Select(attrs={'class':'form-control'}),
            'color':forms.Select(attrs={'class':'form-control'}),
            'bastidor':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_matricula':forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'itv':forms.DateInput(attrs={'type': 'date','class':'form-control'}),

            'odo':forms.NumberInput(attrs={'class':'form-control'}),

        }

