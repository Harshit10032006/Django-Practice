from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.

def post(request):
   query = request.GET.get('q')
   category = request.GET.get('category')
   if query:
      posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
   else:
      posts = Post.objects.all()
   
   if category:
      posts = posts.filter(category=category)
   
   return render(request, 'post.html', {'posts': posts, 'query': query, 'category': category})