# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('urlone', models.CharField(max_length=450)),
                ('urltwo', models.CharField(max_length=450)),
                ('urlthere', models.CharField(max_length=450)),
            ],
        ),
    ]
