# Generated by Django 5.0.6 on 2024-05-16 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_store_app', '0008_alter_customerorder_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='vehicles_owned',
            field=models.ManyToManyField(to='cycling_store_app.vehicle'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 16, 10, 22, 56, 155713)),
        ),
    ]