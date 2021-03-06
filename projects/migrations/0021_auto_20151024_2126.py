# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20151024_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user_student',
            field=models.ManyToManyField(related_name='student_user', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
