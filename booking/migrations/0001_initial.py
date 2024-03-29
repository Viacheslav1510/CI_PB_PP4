# Generated by Django 3.2.18 on 2023-03-10 16:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Dingle Trip', 'Doctor care'), ('Ring Of Kerry', 'Nursing care'), ('The Skellig Ring', 'The Skellig Ring'), ('Homemaker or basic assistance care', 'Homemaker or basic assistance care')], default='Doctor care', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('8 PM', '8 PM'), ('10 PM', '10 PM'), ('12 PM', '12 PM'), ('14 PM', '14 PM'), ('16', '16 PM')], default='8 PM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
