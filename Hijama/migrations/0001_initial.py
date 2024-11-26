# Generated by Django 5.1.3 on 2024-11-26 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Main', '0003_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], default=1)),
                ('has_diabetes', models.IntegerField(choices=[(1, 'Yes'), (0, 'No'), (-1, 'Unaware')], default=0)),
                ('blood_pressure', models.IntegerField(choices=[(0, 'Normal'), (1, 'Low'), (2, 'High'), (-1, 'Unaware')], default=0)),
                ('health_issues', models.TextField(default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hijama_assessments', to='Main.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]