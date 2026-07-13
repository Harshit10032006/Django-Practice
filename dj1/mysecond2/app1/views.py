from multiprocessing import context

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class View :
    def __init__ (self,age,name,gender):
        self.age = age
        self.name = name
        self.gender = gender
    
def home (request):
        context={'name':'Johnny','age':20,'gender':'Male',
                 'skills':['Python','Django','React'],
                 'user':View(30,'John','Male'),
                 'app1':{
                     'title':'My First App',
                     'content':'This is my first app using Django framework',
                     'created_at':'2023-01-01',
                 }}
        return render(request,'home.html',context)