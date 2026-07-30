from django.shortcuts import render
from .models import user_list
# Create your views here.
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 15) 
def index(request):
    if not cache.get('users'):
        print('Fetching from database')
        users = user_list.objects.all()
        cache.set('users', users, 60 * 15)
    else:
        print('Fetching from cache')
        users = cache.get('users')
    return render(request, 'index.html', {'users': users})
    
