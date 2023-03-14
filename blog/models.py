from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(blank=False)
    excerpt = models.TextField(max_length=200, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    featured_image = CloudinaryField(
        'blog_image',
        default=None,
        null=True,
        blank=True
    )  # models.ImageField(upload_to='blog_image', blank=True)
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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
