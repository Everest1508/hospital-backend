# Generated by Django 5.0.1 on 2024-02-04 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_alter_room_bed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='bed',
        ),
        migrations.AddField(
            model_name='bed',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
    ]
