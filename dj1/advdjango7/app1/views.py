from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list") # this moves in post_list
    
