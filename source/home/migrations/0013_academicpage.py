# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0012_staffpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', auto_created=True, primary_key=True, parent_link=True)),
                ('subsection_title', models.CharField(default='title goes here', max_length=30, help_text='maximum length of 30 characters')),
                ('subsection_subtitle', models.CharField(default='subtitle goes here', max_length=100, help_text='maximum length of 100 characters')),
                ('body', wagtail.wagtailcore.fields.RichTextField(default='Academics....')),
                ('main_image', models.ForeignKey(help_text='Image size must be 750 x 300 (width x height)', to='wagtailimages.Image', related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
