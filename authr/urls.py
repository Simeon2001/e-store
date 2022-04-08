from django.urls import path
from authr import views
from authr.views import UserCreateView


urlpatterns = [
    path("token", views.authrtoken, name="token/"),
    path("register", UserCreateView.as_view(), name="register/"),
]
