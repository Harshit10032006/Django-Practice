from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('submit/', views.submit_form, name='submit_form'),
]