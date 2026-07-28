from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def send_emails(request):
    send_mail(
        'Subject is trying django for mailsw', # subject 
        'Message WOW its working finally second', # message
        'harshitkholiya1003@gmail.com', # from email
        ['harshitkholiya34@gmail.com','manan230111@gmail.com'], # to email
        fail_silently=False,
    )
    return HttpResponse('Email sent successfully!')



def send_html_email(request):
    html_content = render_to_string(
        'emial/welcome.html',
        {'name': 'Harshit'}
    )

    sent = send_mail(
        'Welcome to Django',
        'Plain text version',
        'harshitkholiya1003@gmail.com',
        ['harshitkholiya34@gmail.com', 'manan230111@gmail.com'],
        fail_silently=False,
        html_message=html_content,
    )

    return HttpResponse(f"Emails sent: {sent}")
