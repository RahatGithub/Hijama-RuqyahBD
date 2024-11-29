# Generated by Django 5.1.3 on 2024-11-26 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hijama', '0001_initial'),
        ('Main', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='Main.appointment'),
        ),
    ]