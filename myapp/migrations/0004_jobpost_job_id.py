# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150828_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='job_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
