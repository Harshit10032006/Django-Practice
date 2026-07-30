from django.shortcuts import render
from .models import MyModel

# Create your views here.

from django.core.cache import cache


def index(request):
    users = cache.get('users')
    if not users:
        users = list(MyModel.objects.all())
        cache.set('users', users, 60 * 15)  # Cache for 15 minutes
    return render(request, 'index.html', {'users': users})