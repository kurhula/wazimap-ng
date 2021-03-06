# Generated by Django 2.2.10 on 2020-04-10 12:42

from django.db import migrations

def create_metadata(apps, schema_editor):
    Dataset = apps.get_model('datasets', 'Dataset')
    MetaData = apps.get_model('datasets', 'MetaData')

    for dataset in Dataset.objects.all():
        if MetaData.objects.filter(dataset=dataset).count() == 0:
            MetaData.objects.create(dataset=dataset, source="", licence=None, description="")


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0061_auto_20200406_0255'),
    ]

    operations = [
        migrations.RunPython(create_metadata),
    ]
