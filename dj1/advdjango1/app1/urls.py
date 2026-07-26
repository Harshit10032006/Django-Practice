from django.urls import path

from . import views
urlpatterns = [ 
    path('', views.student_create, name='student_create'),
    path('list/', views.student_list, name='student_list'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student')

]
