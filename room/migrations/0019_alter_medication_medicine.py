# Generated by Django 5.0.1 on 2024-02-04 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0018_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medicine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.medicine'),
        ),
    ]