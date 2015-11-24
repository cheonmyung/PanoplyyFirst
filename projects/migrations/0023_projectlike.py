# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0022_auto_20151025_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liked_projects', models.ManyToManyField(related_name='liked_projects', to='projects.Project', blank=True)),
                ('user', models.OneToOneField(related_name='liker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
