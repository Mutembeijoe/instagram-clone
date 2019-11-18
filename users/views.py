from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Create your views here.

class CreateUserView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class DetailUserView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

class UpdateUserView(UpdateView):
    # form_class = CustomUserChangeForm
    # template_name = 'update_user.html'
    # success_url = reverse_lazy('profile')
    model = get_user_model()
    template_name = 'update_user.html'
    fields = ['username', 'email', 'avatar']