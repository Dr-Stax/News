from django.urls import path
from .views import SignUpView, LogoutView, CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = 'signup'),
    path("logout/", LogoutView.as_view(), name = "logout"),
    path("login/", LoginView.as_view(), name = "login"),
    path("change_password/", PasswordChangeView.as_view(template_name = "registration/password_change.html"), name = 'change_password'),
    path("password_change/done", PasswordChangeDoneView.as_view(template_name = "registration/password_change_done.html"), name = "password_change_done"),
    #path("forgotten_password/", PasswordResetView.as_view(template_name = "forgotten_password.html"), name = "fogotten_password")
    path("forgotten_password/", auth_views.PasswordResetView.as_view(), name= 'forgotten')
]