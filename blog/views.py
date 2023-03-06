from django.shortcuts import render, redirect
from .models import PostModel
from .forms import CommentForm, PostModelForm
from django.shortcuts import get_object_or_404
# Create your views here.


def blog_home(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def create_blog(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            # 
        else: 
            messages.errors(request, str(form.errors))
    else:
        form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add-blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments.filter(approved=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()

    context = {
        'post': post,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, "blog/blog-details.html", context)
