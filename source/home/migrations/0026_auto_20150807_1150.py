# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20150807_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjunctprofessor',
            name='professor_course',
            field=models.CharField(verbose_name='Course', max_length=100, help_text='Professor title with maximum length of 100 characters'),
        ),
    ]
