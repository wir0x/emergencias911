# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20161016_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centroemergencia',
            name='direccion',
            field=models.CharField(max_length=150, verbose_name='Dirección'),
        ),
    ]