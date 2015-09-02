# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Anonymous', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('industry', models.TextField(choices=[(b'IT', b'IT'), (b'Healthcare', b'Healthcare'), (b'Finance', b'Medical'), (b'Retail', b'Retail'), (b'Media', b'Media'), (b'Food services', b'Food services'), (b'Other', b'Other')])),
                ('designation', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='JobPost',
        ),
    ]
