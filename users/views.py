# users/views.py

from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# Create your views here.

class DashboardView(TemplateView):
    template_name = "users/dashboard.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

