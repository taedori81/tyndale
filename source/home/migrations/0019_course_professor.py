# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0018_facultyprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=30, help_text='Profile name with maximum length of 30 characters', verbose_name='Name')),
                ('profile_title', models.CharField(max_length=100, help_text='Profile title with maximum length of 100 characters', verbose_name='Title')),
                ('profile_spec', wagtail.wagtailcore.fields.RichTextField(verbose_name='Spec')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.Course')),
                ('profile_image', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+')),
            ],
        ),
    ]
