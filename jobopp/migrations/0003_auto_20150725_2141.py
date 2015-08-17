# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobopp', '0002_post_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='text', max_length=200),
            preserve_default=False,
        ),
    ]
