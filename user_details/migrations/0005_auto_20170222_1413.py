# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0004_merge_20170222_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='user_id',
            field=models.IntegerField(default=True, primary_key=True, serialize=False),
        ),
    ]