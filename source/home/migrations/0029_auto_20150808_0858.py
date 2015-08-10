# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20150807_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='slider2_header1',
            field=models.CharField(default='This displays bible verse', max_length=255, help_text='maximum length of 100 characters'),
        ),
    ]
