# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monograph',
            name='primary_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monograph',
            name='secondary_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
