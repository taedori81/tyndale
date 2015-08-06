# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0015_facultypage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True, serialize=False)),
                ('subsection_title', models.CharField(default='title goes here', help_text='maximum length of 30 characters', max_length=30)),
                ('subsection_subtitle', models.CharField(default='subtitle goes here', help_text='maximum length of 100 characters', max_length=100)),
                ('body', wagtail.wagtailcore.fields.RichTextField(default='About admission....')),
                ('main_image', models.ForeignKey(related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True, help_text='Image size must be 750 x 300 (width x height)')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
