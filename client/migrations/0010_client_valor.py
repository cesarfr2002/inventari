# Generated by Django 4.2.11 on 2024-11-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_remove_client_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='valor',
            field=models.IntegerField(null=True),
        ),
    ]
