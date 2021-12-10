from django.urls import path
from facebook.views import index,home

urlpatterns = [
    path('index', index),
    path('home', home)
]
