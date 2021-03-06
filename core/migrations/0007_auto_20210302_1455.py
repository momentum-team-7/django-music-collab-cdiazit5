# Generated by Django 3.1.7 on 2021-03-02 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210301_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='core.artist'),
        ),
    ]
