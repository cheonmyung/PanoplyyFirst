# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20151025_1335'),
        ('trys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMarks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='projects.Project')),
                ('project_like_user', models.ForeignKey(to='trys.ProjectLike')),
            ],
        ),
    ]
