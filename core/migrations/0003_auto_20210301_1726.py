# Generated by Django 3.1.7 on 2021-03-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
