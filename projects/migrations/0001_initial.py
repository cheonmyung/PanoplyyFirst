# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('position_summary', models.TextField(max_length=300)),
                ('deliverables', models.TextField(max_length=300)),
                ('submission', models.CharField(max_length=300)),
                ('comments', models.TextField(null=True, blank=True)),
                ('job_category', models.CharField(blank=True, max_length=50, null=True, choices=[(b'Business', b'Business'), (b'Marketing', b'Marketing'), (b'Computer Science', b'Computer Science'), (b'Engineering', b'Engineering'), (b'Health', b'Health'), (b'NewsMedia', b'NewsMedia'), (b'Psychology', b'Psychology'), (b'Trade', b'Trade')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('user_company', models.ForeignKey(related_name='company_user', to=settings.AUTH_USER_MODEL)),
                ('user_student', models.ManyToManyField(related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
