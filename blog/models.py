# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostModel(models.Model):
    """
    A class to create Post model
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(blank=False)
    excerpt = models.TextField(max_length=300, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    featured_image = CloudinaryField(
        'blog_image',
        null=True,
        blank=False,
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.slug)])

    def comment_count(self):
        return self.comment_set.filter(approved=True).count()

    def comments(self):
        return self.comment_set.filter(approved=True)


class Comment(models.Model):
    """
    A class to create Comment model
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    body = models.CharField(blank=False, max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'Comment {self.body} by {self.user.username}'
