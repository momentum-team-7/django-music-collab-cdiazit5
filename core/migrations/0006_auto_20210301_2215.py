# Generated by Django 3.1.7 on 2021-03-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=75),
        ),
    ]
