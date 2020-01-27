"""alquiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import  DetalleVehiculo,ListaDeVehiculos,ActulizarVehiculo, CrearVehiculo, ListaDeVehiculosSalamanca, ListaDeVehiculosMadrid, ListaDeVehiculosValladolid,ListaDeVehiculosMallorca, ListaDeVehiculosLasPalmas, ListaDeVehiculosZamora,Foto

vehiculo_patterns = ([
    
    path("",ListaDeVehiculos.as_view(), name="flota"),
    path('<int:pk>/<slug:slug>/', DetalleVehiculo.as_view(), name='detalle'),
    path('Crear/', CrearVehiculo.as_view(), name='crear'),
    path('Actualizar/<int:pk>', ActulizarVehiculo.as_view(), name='actualizar'),
    path("Salamanca/",ListaDeVehiculosSalamanca.as_view(), name="flotasalamanca"),
    path("Madrid/",ListaDeVehiculosMadrid.as_view(), name="flotamadrid"),
    path("Valladolid/",ListaDeVehiculosValladolid.as_view(), name="flotavalladolid"),
    path("Mallorca/",ListaDeVehiculosMallorca.as_view(), name="flotamallorca"),
    path("LasPalmas/",ListaDeVehiculosLasPalmas.as_view(), name="flotalaspalmas"),
    path("Zamora/",ListaDeVehiculosZamora.as_view(), name="flotazamora"),
    path("SubirFoto/",Foto.as_view(),name='subirfoto'),
    



    ],'vehiculo')