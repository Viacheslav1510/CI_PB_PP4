# Generated by Django 3.2.18 on 2023-03-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20230313_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(default='kerry tour', max_length=500),
        ),
    ]
