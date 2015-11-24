# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20151013_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='overview',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
    ]
