# Generated by Django 3.2.18 on 2023-03-11 16:20

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='day',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='service',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='time',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='time_ordered',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='user',
        ),
        migrations.AddField(
            model_name='tour',
            name='max_seats',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='tour_image'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Please enter a valid phone number,e.g. 123456789. Up to 15 digits allowed.', regex='^\\+?1?\\d{8,15}$')])),
                ('time', models.CharField(choices=[('8 PM', '8 PM'), ('10 PM', '10 PM'), ('12 PM', '12 PM'), ('14 PM', '14 PM'), ('16 PM', '16 PM')], default='8 PM', max_length=10)),
                ('tour_date', models.DateField()),
                ('number_of_seats', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
