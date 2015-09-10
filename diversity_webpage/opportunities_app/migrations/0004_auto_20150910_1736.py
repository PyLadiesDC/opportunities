# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities_app', '0003_auto_20150910_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='benefits',
            field=models.TextField(help_text=b'What are the benefits this opportunity    provides.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='compensation_amount',
            field=models.CharField(default='$0/hr', help_text=b'Dollars/time period', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='compensation_type',
            field=models.CharField(default='s', help_text=b'Type of compensation', max_length=1, choices=[(b'h', b'Hourly'), (b's', b'Salary')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='expiration',
            field=models.DateTimeField(help_text=b'Expiration date of posting', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='filled_opportunity',
            field=models.BooleanField(default=False, help_text=b'Was this opportunity filled?'),
        ),
        migrations.AddField(
            model_name='post',
            name='organization_name',
            field=models.CharField(help_text=b'Name of company or organization', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text=b'What is the job description?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='point_of_contact',
            field=models.CharField(help_text=b'Person to contact', max_length=100),
        ),
    ]
