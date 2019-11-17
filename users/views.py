from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.

class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')