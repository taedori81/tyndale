# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20150807_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyprofile',
            name='page',
        ),
        migrations.RemoveField(
            model_name='facultyprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='facultypage',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Course', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Professor', blank=True, related_name='+'),
        ),
        migrations.DeleteModel(
            name='FacultyProfile',
        ),
    ]
