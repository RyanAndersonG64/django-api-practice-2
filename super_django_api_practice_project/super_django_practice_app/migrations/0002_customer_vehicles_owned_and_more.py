# Generated by Django 5.0.6 on 2024-05-21 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_django_practice_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='vehicles_owned',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 21, 11, 14, 48, 618743)),
        ),
    ]
