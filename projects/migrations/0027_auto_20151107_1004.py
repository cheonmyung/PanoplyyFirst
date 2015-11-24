# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20151106_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='job_type',
            field=models.CharField(max_length=50, choices=[(b'Internship', b'Internship'), (b'Entry-Level Job', b'Entry-Level Job')]),
        ),
    ]
