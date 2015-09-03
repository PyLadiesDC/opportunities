# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=datetime.datetime(2015, 7, 22, 20, 59, 18, 856570, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
