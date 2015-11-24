# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20151023_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 4, 7, 27, 28190, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 4, 7, 27, 27804, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
