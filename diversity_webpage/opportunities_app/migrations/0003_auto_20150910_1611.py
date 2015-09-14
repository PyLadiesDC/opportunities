# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities_app', '0002_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone',
        ),
        migrations.AddField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 16, 11, 8, 196149, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(help_text=b'Address of the business', max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(help_text=b'Title of the job post', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='point_of_contact',
            field=models.CharField(help_text=b'Posting contact point', max_length=100),
        ),
    ]
