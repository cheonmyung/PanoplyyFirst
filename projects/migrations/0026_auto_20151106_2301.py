# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20151106_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='position_category',
            field=models.CharField(max_length=200),
        ),
    ]
