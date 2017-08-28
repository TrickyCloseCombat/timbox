# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20170827_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='title',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
