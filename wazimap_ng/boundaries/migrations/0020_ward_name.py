# Generated by Django 2.2.8 on 2020-01-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0019_auto_20200125_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='name',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
