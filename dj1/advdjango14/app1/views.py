from django.shortcuts import render
from .models import user_list
# Create your views here.
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 15) 
def index(request):
    print('Fetching from database')
    users = user_list.objects.all()
    return render(request, 'index.html', {'users': users})
    
