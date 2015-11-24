# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20151023_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 14, 9, 18, 834099, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 24, 4, 9, 18, 834062, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
