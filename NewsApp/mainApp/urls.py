from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('microsoft', views.microsoft, name="microsoft"),
    path('apple', views.apple, name="apple"),
    path('gaming', views.gaming, name="gaming"),
    path('world', views.world, name="world"),
    path('samsung', views.samsung, name="samsung"),
    path('sony', views.sony, name="sony")
]
