# Generated by Django 2.2.10 on 2020-06-10 11:37

import django.core.validators
from django.db import migrations, models
import wazimap_ng.datasets.models.upload


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0102_auto_20200601_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='geographyhierarchy',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
