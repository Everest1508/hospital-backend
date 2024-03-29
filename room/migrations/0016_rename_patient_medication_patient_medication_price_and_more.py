# Generated by Django 5.0.1 on 2024-02-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0015_remove_medication_name_medication_medication_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medication',
            old_name='Patient',
            new_name='patient',
        ),
        migrations.AddField(
            model_name='medication',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='timing',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')], max_length=30, null=True),
        ),
    ]
