# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150805_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main_subheader',
            field=models.CharField(max_length=255, default="mission's description", help_text='maximum length of 255 characters'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slider1_header2',
            field=models.CharField(max_length=50, default='Tyndale international university', help_text='maximum length of 50 characters'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='slider1_subheader1',
            field=models.CharField(max_length=100, default='The reformed theology based seminary', help_text='maximum length of 100 characters'),
        ),
    ]
