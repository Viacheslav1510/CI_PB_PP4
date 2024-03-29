# Generated by Django 3.2.18 on 2023-03-27 20:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_postmodel_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='static/images/kerry.jpg', max_length=255, null=True, verbose_name='blog_image'),
        ),
    ]
