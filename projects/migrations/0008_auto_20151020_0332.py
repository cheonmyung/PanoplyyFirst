# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20151020_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 11, 19, 3, 32, 25, 467578)),
        ),
    ]
