# Generated by Django 3.2.18 on 2023-03-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_postmodel_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='featured_image',
            field=models.ImageField(blank=True, default='/images/man-1.jpg', upload_to='blog_image'),
        ),
    ]
