# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20150807_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='adjunct_faculty',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='professor',
            name='professor_title',
            field=models.CharField(blank=True, verbose_name='Professor Title', max_length=100, help_text='Professor title with maximum length of 100 characters'),
        ),
    ]
