# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('calle', models.CharField(max_length=150)),
                ('colonia', models.CharField(max_length=150)),
                ('numeroExterior', models.CharField(max_length=150)),
                ('numeroInterior', models.CharField(max_length=150)),
                ('codigoPostal', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
            ],
        ),
    ]
