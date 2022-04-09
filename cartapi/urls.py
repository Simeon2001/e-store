from django.urls import path
from . import views

urlpatterns = [
    path ('cart', views.all_order, name = 'Home/' ),
    path('update', views.update, name = 'update/'),
    path('checkout', views.Checkout, name = 'checkout/'),
    
]