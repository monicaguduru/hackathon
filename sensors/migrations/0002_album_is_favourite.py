# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
