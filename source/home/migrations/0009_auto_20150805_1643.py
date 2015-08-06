# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150805_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chairmanpage',
            old_name='main_paragraph',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='presidentpage',
            old_name='main_paragraph',
            new_name='body',
        ),
    ]
