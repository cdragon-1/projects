# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
