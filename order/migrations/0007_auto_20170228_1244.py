# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20170228_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_data_purchase',
            name='payment_description',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order_data_purchase',
            name='payment_status',
            field=models.BooleanField(verbose_name=False),
        ),
        migrations.AlterField(
            model_name='order_data_selling',
            name='payment_description',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order_data_selling',
            name='payment_status',
            field=models.BooleanField(verbose_name=False),
        ),
        migrations.AlterField(
            model_name='order_data_selling',
            name='sub_total',
            field=models.FloatField(max_length=120, null=True),
        ),
    ]