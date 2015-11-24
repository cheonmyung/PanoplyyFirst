# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20151024_0409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_start', '-updated']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=projects.models.after_thirty_days, verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Start Date'),
        ),
    ]
