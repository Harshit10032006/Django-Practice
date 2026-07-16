from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'app1/anything.html')

def base(request):
    return render(request,'home.html')

