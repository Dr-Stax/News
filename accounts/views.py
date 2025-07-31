from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .form import CustomUserCreationForm
from django.contrib.auth.views import LogoutView, PasswordResetView
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")

"""class ResetPassword(PasswordResetView):
    next_page = reverse_lazy("home")"""
