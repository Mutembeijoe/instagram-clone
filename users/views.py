from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.

class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class DetailUserView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'