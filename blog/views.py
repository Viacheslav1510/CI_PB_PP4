from django.shortcuts import render
from .models import PostModel
from django.shortcuts import get_object_or_404
# Create your views here.


def blog_home(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    return render(request, "blog/blog-details.html", {'post': post})
