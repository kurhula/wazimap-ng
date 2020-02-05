# Generated by Django 2.2.8 on 2020-02-04 17:37

import django.core.validators
from django.db import migrations, models
import wazimap_ng.datasets.models.upload


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0027_auto_20200204_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(help_text='\n            Uploaded document should be less than 20.0 MiB in size and \n            file extensions should be one of xls, xlsx, csv.\n        ', upload_to='datasets/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx', 'csv']), wazimap_ng.datasets.models.upload.file_size])),
            ],
        ),
    ]
