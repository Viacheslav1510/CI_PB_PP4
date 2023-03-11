# Generated by Django 3.2.18 on 2023-03-11 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230311_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='description',
            field=models.CharField(default='kerry tour', max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_seats',
            field=models.CharField(choices=[(1, 'One Seat'), (2, 'Two seats'), (3, 'Three seats'), (4, 'Four seats'), (5, 'Four seats')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('8 AM', '8 AM'), ('10 AM', '10 AM'), ('12 PM', '12 PM'), ('14 PM', '14 PM')], default='8 PM', max_length=10),
        ),
    ]
