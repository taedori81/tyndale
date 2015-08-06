# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0014_academicprogrampage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', parent_link=True, auto_created=True, primary_key=True, serialize=False)),
                ('subsection_title', models.CharField(max_length=30, default='title goes here', help_text='maximum length of 30 characters')),
                ('subsection_subtitle', models.CharField(max_length=100, default='subtitle goes here', help_text='maximum length of 100 characters')),
                ('tab_title_1', models.CharField(max_length=30, default='tab title goes here', help_text='maximum length of 30 characters')),
                ('tab_title_2', models.CharField(max_length=30, default='tab title goes here', help_text='maximum length of 30 characters')),
                ('subject_name_1', models.CharField(max_length=50, default='Biblical Theology / Biblical Languages', help_text='maximum length of 50 characters')),
                ('subject_name_2', models.CharField(max_length=50, default='Hermeneutics / Christian Counseling', help_text='maximum length of 50 characters')),
                ('subject_name_3', models.CharField(max_length=50, default='Christian Education', help_text='maximum length of 50 characters')),
                ('subject_name_4', models.CharField(max_length=50, default='Church History/Historical Theology', help_text='maximum length of 50 characters')),
                ('subject_name_5', models.CharField(max_length=50, default='Church Music', help_text='maximum length of 50 characters')),
                ('subject_name_6', models.CharField(max_length=50, default='Church Ministry/Practical Theology', help_text='maximum length of 50 characters')),
                ('subject_name_7', models.CharField(max_length=50, default='Christian Evangelism / Missiology', help_text='maximum length of 50 characters')),
                ('subject_name_8', models.CharField(max_length=50, default='Systematic Theology/Apologetics', help_text='maximum length of 50 characters')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
