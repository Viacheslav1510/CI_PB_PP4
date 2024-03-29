# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import PostModel
from .forms import CommentForm, PostModelForm, PostUpdateForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def blog_home(request):
    """
    A function to open blog page,
    provide existent posts and make pagination
    """
    posts = PostModel.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/blog.html', context)


@login_required
def post_details(request, slug):
    """
    A function to open post details page,
    provide comment form and show existent comments
    """
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.comments
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            form.save()
            messages.info(request, "You've left comment successfully")
            return redirect('blog-detail', slug=post.slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, "blog/blog-details.html", context)


@login_required
def create_post(request):
    """
    A function to open post creation page
    and provide post creation form
    """
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.info(request, "The post have been created")
            return redirect('blog')
    else:
        form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'blog/add-blog.html', context)


@login_required
def edit_post(request, slug):
    """
    A function to open post edit page
    and provide post edit form
    """
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, "The post have been updated")
            return redirect('blog-detail', slug=post.slug)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/edit-blog.html', context)


@login_required
def delete_post(request, slug):
    """
    A function to open post delete confirmation page
    """
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.info(request, "The post have been deleted")
        return redirect('blog')
    context = {
        'post': post,
    }
    return render(request, 'blog/delete-blog.html', context)
