from app1.views import index
from django.urls import path

urlpatterns = [
    path('index/', index),
]