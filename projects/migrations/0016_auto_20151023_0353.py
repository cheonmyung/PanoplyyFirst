# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20151022_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 3, 53, 19, 581729, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AddField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 3, 53, 19, 581493, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
