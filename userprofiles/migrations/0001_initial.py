# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import userprofiles.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('overview', models.CharField(max_length=100, null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=userprofiles.models.upload_profile, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
