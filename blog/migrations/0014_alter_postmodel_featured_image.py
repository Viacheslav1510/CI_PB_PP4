# Generated by Django 3.2.18 on 2023-03-08 11:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_postmodel_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='blog_image'),
        ),
    ]
