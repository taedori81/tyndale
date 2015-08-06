# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0011_auto_20150805_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, to='wagtailcore.Page', parent_link=True)),
                ('subsection_title', models.CharField(max_length=30, default='title goes here', help_text='maximum length of 30 characters')),
                ('subsection_subtitle', models.CharField(max_length=100, default='subtitle goes here', help_text='maximum length of 100 characters')),
                ('first_column_header', models.CharField(max_length=30, default='header goes here', help_text='maximum length of 30 characters')),
                ('first_column_name', models.CharField(max_length=30, default='name goes here', help_text='maximum length of 30 characters')),
                ('first_column_position', models.CharField(max_length=30, default='position goes here', help_text='maximum length of 30 characters')),
                ('first_column_spec', wagtail.wagtailcore.fields.RichTextField(default='Spec')),
                ('second_column_header', models.CharField(max_length=30, default='header goes here', help_text='maximum length of 30 characters')),
                ('second_column_name', models.CharField(max_length=30, default='name goes here', help_text='maximum length of 30 characters')),
                ('second_column_position', models.CharField(max_length=30, default='position goes here', help_text='maximum length of 30 characters')),
                ('second_column_spec', wagtail.wagtailcore.fields.RichTextField(default='Spec')),
                ('third_column_header', models.CharField(max_length=30, default='header goes here', help_text='maximum length of 30 characters')),
                ('third_column_name', models.CharField(max_length=30, default='name goes here', help_text='maximum length of 30 characters')),
                ('third_column_position', models.CharField(max_length=30, default='position goes here', help_text='maximum length of 30 characters')),
                ('fourth_column_header', models.CharField(max_length=30, default='header goes here', help_text='maximum length of 30 characters')),
                ('fourth_column_name', models.CharField(max_length=30, default='name goes here', help_text='maximum length of 30 characters')),
                ('fourth_column_position', models.CharField(max_length=30, default='position goes here', help_text='maximum length of 30 characters')),
                ('fifth_column_header', models.CharField(max_length=30, default='header goes here', help_text='maximum length of 30 characters')),
                ('fifth_column_name', models.CharField(max_length=30, default='name goes here', help_text='maximum length of 30 characters')),
                ('fifth_column_position', models.CharField(max_length=30, default='position goes here', help_text='maximum length of 30 characters')),
                ('fifth_column_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', help_text='Image size must be 324 x 324 (width x height)', null=True)),
                ('first_column_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', help_text='Image size must be 324 x 324 (width x height)', null=True)),
                ('fourth_column_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', help_text='Image size must be 324 x 324 (width x height)', null=True)),
                ('second_column_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', help_text='Image size must be 324 x 324 (width x height)', null=True)),
                ('third_column_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', help_text='Image size must be 324 x 324 (width x height)', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
