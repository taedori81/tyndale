# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0006_presidentpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChairmanPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
                ('subsection_title', models.CharField(help_text='maximum length of 30 characters', max_length=30, default='title goes here')),
                ('subsection_subtitle', models.CharField(help_text='maximum length of 100 characters', max_length=100, default='subtitle goes here')),
                ('chairman_name', models.CharField(help_text='maximum length of 30 characters', max_length=30, default='chairman name goes here')),
                ('chairman_title', models.CharField(help_text='maximum length of 20 characters', max_length=20, default='chairman title goes here')),
                ('main_paragraph', wagtail.wagtailcore.fields.RichTextField(default='Welcome message of chairman..')),
                ('chairman_image', models.ForeignKey(null=True, help_text='Image size must be 340 x 480 (width x height)', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='main_paragraph',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='body',
            field=models.TextField(default='About Tyndale....'),
        ),
    ]
