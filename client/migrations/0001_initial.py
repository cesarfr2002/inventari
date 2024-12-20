# Generated by Django 5.1.3 on 2024-11-13 19:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('card', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='La cédula debe contener solo números', regex='^\\d+$')])),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El teléfono debe contener solo números', regex='^\\d+$')])),
                ('date', models.DateField()),
                ('medical_prescription', models.CharField(max_length=200)),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
    ]
