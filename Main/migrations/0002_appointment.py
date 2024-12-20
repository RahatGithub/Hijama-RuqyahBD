# Generated by Django 5.1.3 on 2024-11-26 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.IntegerField(choices=[(1, 'Hijama'), (2, 'Ruqyah'), (31, 'Counseling Live'), (32, 'Counseling Online'), (41, 'Assessment Live'), (42, 'Assessment Online')])),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Confirmed'), (2, 'Closed'), (-1, 'Cancelled')], default=0)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Main.user')),
            ],
            options={
                'ordering': ['-date', '-time'],
            },
        ),
    ]
