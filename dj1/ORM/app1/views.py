from django.shortcuts import render
from . models import Customer
# Create your views here.

def app(request):
    return render(request,'app1/app.html')

def customer(request):
    customers=Customer.objects.all()
    return render(request,'app1/app.html')