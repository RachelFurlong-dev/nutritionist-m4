from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from .models import Post
# Create your views here.

def view_blog(request):
    posts = Post.objects.all()
    template = 'blog/blog.html'
    context = {
        'posts':posts,
    }
    return render(request, template, context)
