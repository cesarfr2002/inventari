# Generated by Django 5.1.3 on 2024-11-13 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El teléfono debe contener solo números', regex='^\\d+$')])),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
    ]
