# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20150807_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicPrograms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=50)),
                ('program_description', wagtail.wagtailcore.fields.RichTextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_1',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_2',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_3',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_4',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_5',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_6',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_body_7',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_1',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_2',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_3',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_4',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_5',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_6',
        ),
        migrations.RemoveField(
            model_name='academicprogrampage',
            name='program_title_7',
        ),
    ]
