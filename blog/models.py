from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    rating = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return self.title