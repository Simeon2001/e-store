from django.urls import path
from . import views

urlpatterns = [
    path ('product', views.all_Product, name = 'Home/' ),
    
]