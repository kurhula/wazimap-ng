# Generated by Django 2.2.8 on 2020-01-20 16:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=25)),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=-1)),
            ],
        ),
    ]