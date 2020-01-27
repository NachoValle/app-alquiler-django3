from django.db import models

from django.utils import timezone
from datetime import timedelta, date

from agencia.models import Agencia 



CAR_COLOR = (
        ('RO', 'Rojo'),
        ('NE', 'Negro'),
        ('BA', 'Blanco'),
        ('GC', 'Gris Claro'),
        ('GO', 'Gris Oscuro'),
        ('AZ', 'Azul'),
        ('AM', 'Amarillo'),
        ('NA', 'Naranja'),
        ('OT', 'Otro'),
    )
CAR_FUEL = (
        ('GAS', 'Gasolina'),
        ('DSL', 'Diesel'),
        ('HIB', 'Hibrido'),
        ('GPL', 'GPL'),
    )
CAR_TYPE=(('TU','Turismo'),
          ('FU','Carga'),
    )
class SubirImagen(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    foto = models.ImageField(upload_to='vehiculos',verbose_name='Foto')

class Vehiculo(models.Model):
    
    activo = models.BooleanField(default=True,verbose_name='Activado')
    ciudad = models.ForeignKey(Agencia,on_delete=models.PROTECT)
    tipo = models.CharField(max_length=20,choices=CAR_TYPE)
    placa = models.CharField(max_length=10,  verbose_name='Matrícula')
    marca = models.CharField(max_length=30,verbose_name='Marca')
    modelo = models.CharField(max_length=30, verbose_name='Modelo')
    combustible = models.CharField(max_length=20, choices=CAR_FUEL, verbose_name='Combustible')
    color = models.CharField(max_length=20,choices=CAR_COLOR)
    bastidor = models.CharField(max_length=30,blank=True,null=True)
    fecha_matricula = models.DateField(verbose_name= 'Año matriculación', max_length=200,default=date.today)
    itv = models.DateField(verbose_name= 'I.T.V.', default=date.today)
    image = models.ImageField(verbose_name='imagen',upload_to='vehiculos',default='vehiculos/logo.png')
    #foto = models.ForeignKey(SubirImagen,on_delete=models.PROTECT, null=True, blank=True)
    odo = models.PositiveIntegerField(verbose_name='Odometro',null=True, blank=True)
    def save(self):
        
        self.placa =self.placa.upper()
        self.marca =self.marca.upper()
        self.modelo =self.modelo.upper()
        
        super(Vehiculo,self).save()

    
    class Meta:
        ordering = ['itv']
        unique_together =('placa',)
    
    def __str__(self):
        return self.placa

    def itv_pasada(self):

        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # aparte los que no tienen itv para coparar el resto
        if not self.itv:
            return 0
        #itv le quedan mas de 30 dias para caducar
        elif self.itv > proxima:
            return 'style= color:green'                
        #itv quedan menos de 30 dias para caducar
        elif self.itv > ahora:
            return 'style= color:orange'
        # itv caducada
        else:
            return 'style= color:red'
    
