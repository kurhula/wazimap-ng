# Generated by Django 2.2.10 on 2020-03-30 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0052_profile_geography_hierarchy'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='geography_hierarchy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datasets.GeographyHierarchy'),
            preserve_default=False,
        ),
    ]
