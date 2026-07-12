from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('Hello world app2 ')

def about(req):
    a=10**10
    return HttpResponse(f'number is ok {a}')

def trys(req):
    return HttpResponse(F'Hello how are you by boy  ')
