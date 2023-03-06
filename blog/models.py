from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    featured_image = models.ImageField(upload_to='blog_image', blank=True) #CloudinaryField('image', default='placeholder')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
