# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
