from django.db import models

# Create your models here.
class Agencia(models.Model):
    ciudad = models.CharField(unique=True, max_length=50, verbose_name='Ciudad')
    codigo = models.CharField(blank=True,null=True, max_length=2, verbose_name='Codigo Oficina')
    direccion = models.CharField(max_length=200, verbose_name='Dirección')
    codigo_postal = models.FloatField(verbose_name='C.P.')
    telefono_fijo = models.CharField(max_length=20, verbose_name='Teléfono Fijo')
    telefono_movil = models.CharField(max_length=20, verbose_name='Teléfono Móvil')
    email = models.EmailField(max_length=200, verbose_name='Email')
    image = models.ImageField(verbose_name='Avatar',upload_to='Ciudades')
    
    class Meta:
        ordering = ['ciudad']

    def __str__(self):
        return self.ciudad
