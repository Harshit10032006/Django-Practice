from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def set(request):
    request.session['name'] = 'John'
    request.session['age'] = 25
    return HttpResponse("Set data successfully")

def get(request):
    name = request.session.get('name')
    age = request.session.get('age')
    return HttpResponse(f"Get data: {name}, {age}")

def delete(request):
    request.session.flush()
    return HttpResponse("Delete data successfully")
