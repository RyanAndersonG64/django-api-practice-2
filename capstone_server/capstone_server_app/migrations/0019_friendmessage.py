# Generated by Django 5.0.6 on 2024-06-21 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_server_app', '0018_groupmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField(max_length=1000)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_reciever', to='capstone_server_app.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dm_sender', to='capstone_server_app.profile')),
            ],
        ),
    ]
