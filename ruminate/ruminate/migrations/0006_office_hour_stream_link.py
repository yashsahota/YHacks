# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruminate', '0005_auto_20171202_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='office_hour',
            name='stream_link',
            field=models.URLField(blank=True),
        ),
    ]
