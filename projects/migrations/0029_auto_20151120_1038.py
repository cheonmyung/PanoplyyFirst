# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20151111_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='position_category',
            new_name='position_name',
        ),
    ]
