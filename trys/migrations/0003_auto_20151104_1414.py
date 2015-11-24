# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trys', '0002_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectlike',
            name='liked_projects',
        ),
        migrations.RemoveField(
            model_name='projectlike',
            name='user',
        ),
        migrations.AlterField(
            model_name='bookmarks',
            name='project_like_user',
            field=models.ForeignKey(to='projects.ProjectLike'),
        ),
        migrations.DeleteModel(
            name='ProjectLike',
        ),
    ]
