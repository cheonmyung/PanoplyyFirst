# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20151018_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 19, 1, 51, 55, 27743)),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 1, 51, 55, 27712)),
        ),
    ]
