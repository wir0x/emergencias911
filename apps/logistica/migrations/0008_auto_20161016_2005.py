# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0007_tipoincidente_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
