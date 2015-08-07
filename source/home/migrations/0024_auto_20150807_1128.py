# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0023_auto_20150807_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_image',
            field=models.ForeignKey(related_name='+', help_text='Picture must be size of 150 x 200 (width x height)', to='wagtailimages.Image', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
