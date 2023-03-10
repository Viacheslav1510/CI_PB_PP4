# Generated by Django 3.2.18 on 2023-03-04 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230302_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
