from django.shortcuts import render
from .models import PostModel
# Create your views here.


def blog_home(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})