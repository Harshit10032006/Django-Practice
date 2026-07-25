from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models  import contact

# Create your views here.

def form(request):
    return render(request,'form.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        if name and mobile:
            contact.objects.create(name=name, mobile=mobile)
            return HttpResponse(f'Thanks {name}! We have received your mobile number {mobile}.')  
        else :
            return HttpResponse('!!!!*{2}Please provide both name and mobile number!!!!!!')

    redirect('form')  