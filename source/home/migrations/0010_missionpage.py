# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0009_auto_20150805_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, serialize=False, to='wagtailcore.Page', primary_key=True)),
                ('subsection_title', models.CharField(max_length=30, help_text='maximum length of 30 characters', default='title goes here')),
                ('subsection_subtitle', models.CharField(max_length=100, help_text='maximum length of 100 characters', default='subtitle goes here')),
                ('body', wagtail.wagtailcore.fields.RichTextField(default='Welcome message of chairman..')),
                ('main_image', models.ForeignKey(related_name='+', help_text='Image size must be 340 x 480 (width x height)', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
