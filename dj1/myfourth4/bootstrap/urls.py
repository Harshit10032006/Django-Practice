from . import views
from django.urls import path
urlpatterns = [path('',views.home,name='home'),
               path('one/',views.one,name='one'),]