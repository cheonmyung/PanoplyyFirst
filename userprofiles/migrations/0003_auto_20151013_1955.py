# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20151013_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='picture',
        ),
    ]
