# Generated by Django 3.2.18 on 2023-03-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20230314_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_seats',
            field=models.IntegerField(default=1),
        ),
    ]
