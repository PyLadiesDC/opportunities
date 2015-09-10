# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities_app', '0004_auto_20150910_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='token',
            field=models.CharField(default='2390d2e73b386b2f1c2270736986e2b21fa5400eeb0b4a48c54458d99fe13c739eee733bfa38d12bd97ff13fb26c667faf7bc215135f9940eecb2c48d9bf533489b764014d48', unique=True, max_length=100),
            preserve_default=False,
        ),
    ]
