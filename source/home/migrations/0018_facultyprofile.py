# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0017_contactpage_formfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
                ('profile_name', models.CharField(verbose_name='Name', max_length=30, help_text='Profile name with maximum length of 30 characters')),
                ('profile_title', models.CharField(verbose_name='Title', max_length=100, help_text='Profile title with maximum length of 100 characters')),
                ('profile_spec', wagtail.wagtailcore.fields.RichTextField(verbose_name='Spec')),
                ('page', modelcluster.fields.ParentalKey(related_name='faculty_profile', to='home.FacultyPage')),
                ('profile_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
