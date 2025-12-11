from .apps import UsersConfig

app_name = UsersConfig.name
from django.urls import path
from . import views

urlpatterns = [path("signup/", views.signup, name="signup")]
