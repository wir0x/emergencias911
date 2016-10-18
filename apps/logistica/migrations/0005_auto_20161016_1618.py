# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0004_auto_20161015_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoIncidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Descripción')),
            ],
        ),
        migrations.AddField(
            model_name='incidente',
            name='tipo',
            field=models.ManyToManyField(to='logistica.TipoIncidente'),
        ),
    ]