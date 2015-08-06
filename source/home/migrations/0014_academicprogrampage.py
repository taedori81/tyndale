# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0013_academicpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicProgramPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='wagtailcore.Page')),
                ('subsection_title', models.CharField(default='title goes here', help_text='maximum length of 30 characters', max_length=30)),
                ('subsection_subtitle', models.CharField(default='subtitle goes here', help_text='maximum length of 100 characters', max_length=100)),
                ('program_title_1', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_1', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_2', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_2', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_3', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_3', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_4', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_4', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_5', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_5', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_6', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_6', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
                ('program_title_7', models.CharField(default='academic program title goes here', help_text='maximum length of 50 characters', max_length=50)),
                ('program_body_7', wagtail.wagtailcore.fields.RichTextField(default="Program's Description")),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
