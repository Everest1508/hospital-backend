# Generated by Django 5.0.1 on 2024-02-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_remove_room_clean'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]