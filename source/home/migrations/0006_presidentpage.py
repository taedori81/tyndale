# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0005_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresidentPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, to='wagtailcore.Page', parent_link=True, primary_key=True)),
                ('subsection_title', models.CharField(default='title goes here', max_length=30, help_text='maximum length of 30 characters')),
                ('subsection_subtitle', models.CharField(default='subtitle goes here', max_length=100, help_text='maximum length of 100 characters')),
                ('president_name', models.CharField(default='President name goes here', max_length=30, help_text='maximum length of 30 characters')),
                ('president_title', models.CharField(default='President title goes here', max_length=20, help_text='maximum length of 20 characters')),
                ('main_paragraph', wagtail.wagtailcore.fields.RichTextField(default='Welcome message of president..')),
                ('president_image', models.ForeignKey(related_name='+', null=True, to='wagtailimages.Image', help_text='Image size must be 340 x 480 (width x height)', on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
