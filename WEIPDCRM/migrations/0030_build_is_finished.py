# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0029_auto_20190723_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Job Finished'),
        ),
    ]