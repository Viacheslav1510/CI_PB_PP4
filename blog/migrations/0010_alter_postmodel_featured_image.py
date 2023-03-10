# Generated by Django 3.2.18 on 2023-03-07 09:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_postmodel_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='blog_image'),
        ),
    ]
