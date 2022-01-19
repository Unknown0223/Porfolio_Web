from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf', views.pdf, name='pdf'),
]