# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20170726_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(max_length=100000000000),
        ),
    ]
