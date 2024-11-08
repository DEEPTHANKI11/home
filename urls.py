from django.contrib import admin
from django.urls import path, include
from .views import hello_world
urlpatterns = [
    path('deep', hello_world,name="hello"),
    
]