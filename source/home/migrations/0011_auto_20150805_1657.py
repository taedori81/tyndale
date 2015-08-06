# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0010_missionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaithPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page', primary_key=True)),
                ('subsection_title', models.CharField(default='title goes here', max_length=30, help_text='maximum length of 30 characters')),
                ('subsection_subtitle', models.CharField(default='subtitle goes here', max_length=100, help_text='maximum length of 100 characters')),
                ('body', wagtail.wagtailcore.fields.RichTextField(default='Contents of State of faith')),
                ('main_image', models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, help_text='Image size must be 340 x 480 (width x height)', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='missionpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default='Contents of State of mission'),
        ),
    ]
