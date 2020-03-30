# Generated by Django 2.2.10 on 2020-03-30 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0054_profileindicator_choropleth_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileindicator',
            name='choropleth_method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profile.ChoroplethMethod'),
            preserve_default=False,
        ),
    ]
