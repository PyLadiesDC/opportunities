# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150815_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(default=b'Anonymous', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('job_designation', models.TextField(max_length=500)),
                ('industry', models.TextField(choices=[(b'IT', b'IT'), (b'Healthcare', b'Healthcare'), (b'Finance', b'Medical'), (b'Retail', b'Retail'), (b'Media', b'Media'), (b'Food services', b'Food services'), (b'Other', b'Other')])),
                ('job_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
