# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_auto_20151024_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name=b'Start Date'),
        ),
    ]
