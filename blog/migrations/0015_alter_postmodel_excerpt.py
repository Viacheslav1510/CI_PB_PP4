# Generated by Django 3.2.18 on 2023-03-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_postmodel_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='excerpt',
            field=models.TextField(max_length=200),
        ),
    ]
