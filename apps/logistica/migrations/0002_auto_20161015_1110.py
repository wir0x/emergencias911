# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidente',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
