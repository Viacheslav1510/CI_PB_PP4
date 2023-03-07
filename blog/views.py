from django.shortcuts import render, redirect
from .models import PostModel
from .forms import CommentForm, PostModelForm, PostUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


def blog_home(request):
    posts = PostModel.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


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


def create_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog')
    else:
        form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add-blog.html', context)


def edit_post(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', slug=post.slug)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/edit-blog.html', context)


def delete_post(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.info(request, "The post have been deleted")
        return redirect('blog')
    context = {
        'post': post,
    }
    return render(request, 'blog/delete-blog.html', context)
