# Generated by Django 5.0.1 on 2024-02-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0024_rename_test_bill_test_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ImageField(null=True, upload_to='test'),
        ),
    ]