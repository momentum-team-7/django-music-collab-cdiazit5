# Generated by Django 3.1.7 on 2021-03-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_album_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
