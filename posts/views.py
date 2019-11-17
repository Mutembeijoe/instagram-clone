from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image

# Create your views here.


class PostListView(LoginRequiredMixin,ListView):
    model = Image
    template_name= 'home.html'
    login_url = 'login'
