# Generated by Django 5.0.1 on 2024-02-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='clean',
            field=models.BooleanField(),
        ),
    ]
