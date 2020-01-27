from django.urls import path
from .views import ProfileUpdate ,EmailUpdate, ListaPermisosUsuarios, AltaUsuario,ActualizarPermisos

urlpatterns = [
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),
    path('ListaUsuarios/', ListaPermisosUsuarios.as_view(), name='lista_usuarios'),
    path('AltaUsuario/', AltaUsuario.as_view(), name='alta_usuario'),
    path('Permisos/de_<username>/', ActualizarPermisos.as_view(), name='actualizar_permisos')


]