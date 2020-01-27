from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from .models import Profile
from .forms import ProfileForm, EmailForm, UsuariosForm

# Create your views here.
@method_decorator(login_required,name='dispatch')
class AltaUsuario(SuccessMessageMixin,CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('lista_usuarios')
    template_name = 'registration/alta_usuario.html'
    success_message = " Usuario Creado con Exito"

    

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.p_user :
            return super(AltaUsuario,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))




@method_decorator(login_required,name='dispatch')
class ProfileUpdate(UpdateView):
    
    form_class = ProfileForm
    template_name='registration/profile_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        #recuperar el objeto que se va a editar
        profile , created =  Profile.objects.get_or_create(user=self.request.user)
        return profile
"""
@method_decorator(login_required,name='dispatch')
class ProfileUpdate(DetailView):
    
    model = Profile
    template_name='registration/profile_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        #recuperar el objeto que se va a editar
        profile , created =  Profile.objects.get_or_create(user=self.request.user)
        return profile


"""
        
@method_decorator(login_required,name='dispatch')
class EmailUpdate(UpdateView):    
    form_class = EmailForm
    template_name='registration/email_profile_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        #recuperar el objeto que se va a editar        
        return self.request.user

    def get_form(self, form_class= None):
        form = super(EmailUpdate, self).get_form()
        #modificar a tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs = {'class':'form-control mb-2','placeholder':'email'})
        return form
    


@method_decorator(login_required,name='dispatch')
class ActualizarPermisos(SuccessMessageMixin,UpdateView):
    
    form_class = UsuariosForm
    template_name='registration/actualizarpermisos.html'
    success_url = reverse_lazy('lista_usuarios')
    success_message = " Permisos de USUARIO actualizados con Exito"

    def get_object(self):
        return get_object_or_404(Profile, user__username= self.kwargs['username'])



   
@method_decorator(login_required,name='dispatch')
class ListaPermisosUsuarios(ListView):
    model = Profile
    template_name = 'registration/lista_usuarios.html'      

    def dispatch(self,request, *args,**kwargs):
        if request.user.profile.p_user :
            return super(ListaPermisosUsuarios,self).dispatch(request,*args,**kwargs)
        else:
            return redirect(reverse_lazy('home'))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaPermisosUsuarios, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context        
        context['usuarios'] = User.objects.all()
        return context