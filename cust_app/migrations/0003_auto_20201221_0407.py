# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-12-21 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cust_app', '0002_auto_20201219_0708'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='salesdata',
            table='sales_data',
        ),
        migrations.AlterModelTable(
            name='services',
            table='services',
        ),
    ]
