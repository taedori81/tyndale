# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20150807_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultypage',
            name='course',
        ),
        migrations.RemoveField(
            model_name='facultypage',
            name='professor',
        ),
        migrations.AlterField(
            model_name='professor',
            name='professor_title',
            field=models.CharField(default='Professor Title.', max_length=100, verbose_name='Professor Title', help_text='Professor title with maximum length of 100 characters', blank=True),
        ),
    ]
