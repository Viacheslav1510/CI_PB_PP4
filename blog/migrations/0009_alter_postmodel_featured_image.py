# Generated by Django 3.2.18 on 2023-03-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postmodel_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='blog_image'),
        ),
    ]
