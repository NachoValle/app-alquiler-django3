
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.utils import timezone
from datetime import timedelta, date

from .models import Vehiculo,SubirImagen
from agencia.models import Agencia
from .forms import VehiculoForm, VehiculoActualizarForm

# Create your views here.
"""
class StaffRequiredMixin(object):
 
    este mixin requerira que sea miembro del staff
    
    @method_decorator(staff_member_required)
    def dispatch(self,request, *args,**kwargs):
        
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)  

"""
    







@method_decorator(login_required,name='dispatch')
class Foto(CreateView):
    model = SubirImagen
    fields= ['titulo','foto']
    template_name = 'vehiculo/subir_foto.html'
    success_url= reverse_lazy('vehiculo:flota')
@method_decorator(login_required,name='dispatch')
class ListaDeVehiculos(ListView):
    model = Vehiculo      
       
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculos, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context        
        context['vehiculos'] = Vehiculo.objects.filter(activo=True)     
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(itv__gt= proxima ).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(itv__range=[ahora, proxima]).count()

        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)
        
        car_null =Vehiculo.objects.filter(itv__lt=ahora).count()
        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.todas == True:
            return super(ListaDeVehiculos,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required,name='dispatch')
class DetalleVehiculo(DetailView):
    model = Vehiculo
    template_name='vehiculo/detallevehiculo.html'

@method_decorator(login_required,name='dispatch')
class CrearVehiculo(SuccessMessageMixin,CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    
    template_name = 'vehiculo/crearvehiculo.html'
    success_message = " Vehículo Creado con Exito"
    
    def get_success_url(self):
        return reverse_lazy('vehiculo:detalle', args=[self.object.id, self.object.placa,]  )

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.p_vehiculos:
            return super(CrearVehiculo,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))

    

@method_decorator(login_required,name='dispatch')
class ActulizarVehiculo(SuccessMessageMixin,UpdateView):
    model = Vehiculo
    form_class = VehiculoActualizarForm
    template_name = 'vehiculo/actualizarvehiculo.html'
    success_message = " Vehículo Actualizado con Exito"
    
    def get_success_url(self):
        return reverse_lazy('vehiculo:detalle', args=[self.object.id, self.object.placa,]  )




@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosSalamanca(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosSalamanca, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context        
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=2)
        context['ciudad'] = 'Salamanca'       
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=2)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=2)& Q(itv__range=[ahora, proxima])).count()

        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)
        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=2)& Q(itv__lt=ahora)).count()
        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context


    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.salamanca == True:
            return super(ListaDeVehiculosSalamanca,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosMadrid(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosMadrid, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=1)
        context['ciudad'] = 'Madrid'         
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=1)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=1)& Q(itv__range=[ahora, proxima])).count()

        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)
        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=1)& Q(itv__lt=ahora)).count()
        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.madrid == True:
            return super(ListaDeVehiculosMadrid,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosValladolid(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosValladolid, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=3)
        context['ciudad'] = 'Valladolid'   
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=3)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=3)& Q(itv__range=[ahora, proxima])).count()
        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=3)& Q(itv__lt=ahora)).count()        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context    

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.valladolid == True:
            return super(ListaDeVehiculosValladolid,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosMallorca(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosMallorca, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=4)
        context['ciudad'] = 'Palma De Mallorca'   
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=4)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=4)& Q(itv__range=[ahora, proxima])).count()
        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=4)& Q(itv__lt=ahora)).count()        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context 

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.mallorca == True:
            return super(ListaDeVehiculosMallorca,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosLasPalmas(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosLasPalmas, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=5)
        context['ciudad'] = 'Las Palmas de Gran Canaria'   
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=5)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=5)& Q(itv__range=[ahora, proxima])).count()
        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=5)& Q(itv__lt=ahora)).count()        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context 

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.las_palmas == True:
            return super(ListaDeVehiculosLasPalmas,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))
  

@method_decorator(login_required,name='dispatch')
class ListaDeVehiculosZamora(ListView):
    model =Vehiculo
    template_name='vehiculo/vehiculosmadrid.html'   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeVehiculosZamora, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['vehiculos'] = Vehiculo.objects.filter(ciudad_id=6)
        context['ciudad'] = 'Zamora'   
        
        ahora = date.today()
        proxima = ahora + timedelta(days=30)
        # mensaje de itv ok
        car_ok = Vehiculo.objects.filter(Q(ciudad_id=6)& Q(itv__gt= proxima )).count()
        if car_ok > 0:    
            context['itv_ok'] = " Hay {} vehiculos que tiene correcta la I.T.V.".format(car_ok)
        car_next =Vehiculo.objects.filter(Q(ciudad_id=6)& Q(itv__range=[ahora, proxima])).count()
        if car_next > 0:
            context['itv_proxima'] = " Hay {} vehiculo(s) que tienen menos de 30 dias para pasar la I.T.V.".format(car_next)        
        car_null =Vehiculo.objects.filter(Q(ciudad_id=6)& Q(itv__lt=ahora)).count()        
        if car_null > 0 :
            context['itv_caducada'] = " Hay {} vehiculo(s) que tienen CADUCADA la I.T.V.".format(car_null)
       
        return context  

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.zamora == True:
            return super(ListaDeVehiculosZamora,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))
 

