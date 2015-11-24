# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20151104_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='job_category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='submission',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='company_overview',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='how_to_submit',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='job_type',
            field=models.CharField(default=1, max_length=50, choices=[(b'Internship Full-time', b'Internship Full-time'), (b'Internship Part-time', b'Internship Part-time'), (b'Entry-Level Job', b'Entry-Level Job')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='position_category',
            field=models.CharField(default=1, max_length=50, choices=[(b'Internship Full-time', b'Internship Full-time'), (b'Internship Part-time', b'Internship Part-time'), (b'Entry-Level Job', b'Entry-Level Job')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='salary_or_what_we_offer',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='comments',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='deliverables',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='position_summary',
            field=models.TextField(max_length=5000),
        ),
    ]
