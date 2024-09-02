from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("carta/", views.carta, name="carta"),
    path("ubicaciones/", views.ubicaciones, name="ubicaciones")
]