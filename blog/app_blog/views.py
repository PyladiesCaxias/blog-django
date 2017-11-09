from django.shortcuts import render
from app_blog.models import *

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

