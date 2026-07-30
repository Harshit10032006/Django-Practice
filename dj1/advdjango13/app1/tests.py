from django.test import TestCase
from .models import user_profile
# Create your tests here.
from django.core.cache import cache
from django.shortcuts import render

def user_profiles():
    users_data=cache.get('user_data')


    if not users_data:
        print('Failed') 
        users_data = user_profile.objects.all()
        cache.set('user_data', users_data, 60)
    else :
        print('Passed')
    return render('list.html',{'users':users_data})