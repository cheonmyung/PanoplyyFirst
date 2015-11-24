# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_myuser_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='school',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
