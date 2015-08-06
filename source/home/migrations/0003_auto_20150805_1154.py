# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='main_header',
            field=models.CharField(max_length=30, help_text='maximum length of 30 characters', default='our mission'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_subheader',
            field=models.CharField(max_length=255, help_text='maximum length of 30 characters', default="mission's description"),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider1_header1',
            field=models.CharField(max_length=30, help_text='maximum length of 30 characters', default='Welcome to'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider1_header2',
            field=models.CharField(max_length=30, help_text='maximum length of 30 characters', default='Tyndale international university'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider1_subheader1',
            field=models.CharField(max_length=30, help_text='maximum length of 30 characters', default='The reformed theology based seminary'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider2_header1',
            field=models.CharField(max_length=100, help_text='maximum length of 100 characters', default='This displays bible verse'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slider2_subheader1',
            field=models.CharField(max_length=30, help_text='maximum length of 30 characters', default='romans 5:8'),
        ),
    ]
