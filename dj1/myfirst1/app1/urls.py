from . import views
from django.urls import path,re_path
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pp/',views.trys,name='tyrs'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('name/<str:user_name>/', views.name, name='name'),
    path('years/<int:year>/<int:month>/<int:day>/', views.years, name='years'),
    re_path(r'^artical/(?P<post_id>\d+)/$', views.artical, name='post'),  
    ]