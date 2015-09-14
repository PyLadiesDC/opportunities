# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities_app', '0004_auto_20150910_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='compensation_amount',
        ),
        migrations.RemoveField(
            model_name='post',
            name='compensation_type',
        ),
        migrations.AddField(
            model_name='post',
            name='compensation',
            field=models.TextField(help_text=b'What is the pay?', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_compensated',
            field=models.BooleanField(default=False, help_text=b'Is this opportunity paid?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='benefits',
            field=models.TextField(help_text=b'What are the benefits this opportunity provides?', null=True, blank=True),
        ),
    ]
