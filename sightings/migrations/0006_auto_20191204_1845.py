# Generated by Django 3.0 on 2019-12-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0005_auto_20191204_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
