# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobopp', '0003_auto_20150725_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='email', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone',
            field=models.CharField(default='000-000-0000', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='poc',
            field=models.CharField(default='yourname', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='skills',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]
