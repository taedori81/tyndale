# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0024_auto_20150807_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdjunctProfessor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('professor_name', models.CharField(help_text='Professor name with maximum length of 30 characters', max_length=30, default='Professor Name', verbose_name='Professor Name')),
                ('professor_spec', wagtail.wagtailcore.fields.RichTextField(verbose_name='Professor Spec', default='Professor Spec.')),
                ('professor_course', models.CharField(max_length=100, help_text='Professor title with maximum length of 100 characters', verbose_name='Professor Title')),
                ('professor_image', models.ForeignKey(help_text='Picture must be size of 150 x 200 (width x height)', related_name='+', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='professor',
            name='adjunct_faculty',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='professor_title',
        ),
    ]
