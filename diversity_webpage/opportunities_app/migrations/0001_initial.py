# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('point_of_contact', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
