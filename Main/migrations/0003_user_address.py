# Generated by Django 5.1.3 on 2024-11-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=''),
        ),
    ]