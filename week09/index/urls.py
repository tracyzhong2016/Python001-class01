from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('login2', views.login2)
]
