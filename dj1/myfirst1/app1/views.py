from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse("Hello, World! app1")
def about(req):
    a=10**10
    return HttpResponse(f'number is {a}')

def trys(req):
    return HttpResponse(F'Hello how are you ')

def post(request,post_id):
    return HttpResponse(f'Post ID is {post_id}')
def name(request,user_name):
    return HttpResponse(f'Hello {user_name}!')

def artical(request,post_id):
    return HttpResponse(f'Artical ID is {post_id}')
# def years(request,year,month,day):
#     return HttpResponse(f'Year is {year},month is {month},day is {day} so total is {day}/{month}/{year}')

def years(request,**kwargs):
    year=kwargs['year']
    month=kwargs['month']   
    day=kwargs['day']
    return HttpResponse(f'{kwargs}')