# Generated by Django 5.0.6 on 2024-05-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_store_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.TextField(max_length=100),
        ),
    ]