# Generated by Django 5.0.1 on 2024-02-04 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_alter_bed_bed_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bed',
            name='patient',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.patient'),
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('timing', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('Patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='room.patient')),
            ],
        ),
    ]