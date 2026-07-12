from . import views
from django.urls import path
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pp/',views.trys,name='tyrs')
    ]