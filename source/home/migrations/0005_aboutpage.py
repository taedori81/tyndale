# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0004_auto_20150805_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('subsection_title', models.CharField(help_text='maximum length of 30 characters', max_length=30, default='title goes here')),
                ('subsection_subtitle', models.CharField(help_text='maximum length of 100 characters', max_length=100, default='subtitle goes here')),
                ('main_paragraph', wagtail.wagtailcore.fields.RichTextField(default='About Tyndale....')),
                ('main_image', models.ForeignKey(help_text='Image size must be 750 x 300 (width x height)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
