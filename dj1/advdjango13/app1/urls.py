
from django.urls import path
from .views import user_profiles

urlpatterns=[
    path('',user_profiles,name='user_profiles')
]