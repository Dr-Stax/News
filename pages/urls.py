from django.urls import path
from .views import HomePageView, logo_view


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("logo/", logo_view, name='logo')
]

