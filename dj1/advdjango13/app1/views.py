from django.shortcuts import render
from .models import user_profile
# Create your views here.
from django.core.cache import cache

def user_profiles(request):
    users_data=cache.get('user_data')


    if not users_data:
        print('Failed') 
        users_data = user_profile.objects.all()
        cache.set('user_data', users_data, 60)
    else :
        print('Passed')
    return render(request,'list.html',{'users':users_data})