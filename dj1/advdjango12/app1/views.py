from django.shortcuts import render
from .models import Youtubeuser
from django.core.cache import cache
# Create your views here.


def list(request):
    users = cache.get('users')

    if not users:
        users = Youtubeuser.objects.all()
        cache.set('users', users, 60 * 15)
        print('cache miss')
    else: 
        print('cache hit ')
    return render(request, 'list.html', {'users': users})