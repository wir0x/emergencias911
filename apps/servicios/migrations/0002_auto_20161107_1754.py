# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centroemergencia',
            name='tipo',
            field=models.CharField(choices=[('SALUD', 'SALUD'), ('SEGURIDAD', 'SEGURIDAD'), ('BOMBEROS', 'BOMBEROS'), ('TRANSITO', 'TRANSITO')], max_length=20, verbose_name='Tipo'),
        ),
    ]
