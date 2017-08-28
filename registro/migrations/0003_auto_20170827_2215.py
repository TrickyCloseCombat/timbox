# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='numeroExterior',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='numeroInterior',
            field=models.CharField(max_length=150, blank=True),
        ),
    ]
