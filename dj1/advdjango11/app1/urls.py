from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_emails, name='send_email'),
    path('send-html-email/', views.send_html_email, name='send_html_email'),
]
