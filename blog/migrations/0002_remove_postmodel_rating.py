# Generated by Django 3.2.18 on 2023-03-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='rating',
        ),
    ]
