from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk = instance.pk)
    
    old_instance.avatar_user.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_user = models.ImageField(upload_to=custom_upload_to, null= True, blank= True,verbose_name='Avatar')
    madrid = models.BooleanField(default=False,verbose_name='Madrid')
    salamanca = models.BooleanField(default=False,verbose_name='Salamanca')
    valladolid = models.BooleanField(default=False,verbose_name='Valladolid')
    las_palmas = models.BooleanField(default=False,verbose_name='Las Palmas')
    mallorca = models.BooleanField(default=False,verbose_name='Mallorca')
    zamora = models.BooleanField(default=False,verbose_name='Zamora')
    todas = models.BooleanField(default=False,verbose_name='Todas')
    movil = models.CharField(max_length=20, null= True, blank= True,verbose_name='Télefono Movil')
    p_user = models.BooleanField(default=False,verbose_name='Permisos Usuarios')
    p_vehiculos = models.BooleanField(default=False,verbose_name='Crear Vehiculos')
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
@receiver(post_save, sender = User )
def ensurace_perfil_exists(sender, instance, **kwargs):
    """
    crea un perfil automaticamente al dar de alta un usuario
    """
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('se ha creado un usuario y se ha enlzado un perfil')

    

