# Generated by Django 3.0 on 2019-12-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(max_length=30),
        ),
    ]