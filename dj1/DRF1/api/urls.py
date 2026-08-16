from app1.views import index,person
from django.urls import path
from app1.views import PersonApi

urlpatterns = [
    path('index/', index),
    path('person/',person),
    path('persons/',PersonApi.as_view())
]