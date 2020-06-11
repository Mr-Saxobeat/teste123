from django.shortcuts import render
from .models import Post

# def all_blogs(request):
#     return render(request, 'blog/all_blogs.html')

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
