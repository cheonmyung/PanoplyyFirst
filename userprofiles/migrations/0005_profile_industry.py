# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20151106_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
