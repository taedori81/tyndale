# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_course_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='profile_name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='profile_spec',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='profile_title',
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_name',
            field=models.CharField(max_length=30, default='Professor Name', help_text='Professor name with maximum length of 30 characters', verbose_name='Professor Name'),
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_spec',
            field=wagtail.wagtailcore.fields.RichTextField(default='Professor Spec.', verbose_name='Professor Spec'),
        ),
        migrations.AddField(
            model_name='professor',
            name='professor_title',
            field=models.CharField(max_length=100, default='Professor Title.', help_text='Professor title with maximum length of 100 characters', verbose_name='Professor Title'),
        ),
    ]
