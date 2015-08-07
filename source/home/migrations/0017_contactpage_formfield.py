# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('home', '0016_admissionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', auto_created=True, parent_link=True, serialize=False, primary_key=True)),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to this address', verbose_name='To address', max_length=255)),
                ('from_address', models.CharField(blank=True, verbose_name='From address', max_length=255)),
                ('subject', models.CharField(blank=True, verbose_name='Subject', max_length=255)),
                ('contact_header', models.CharField(help_text='maximum length of 30 characters', default='Contact Us', max_length=30)),
                ('contact_subheader', models.CharField(help_text='maximum length of 100 characters', default='Fill in the form below to get in touch with us.', max_length=100)),
                ('thank_you_text', models.CharField(help_text='maximum length of 255 characters', default='Thank you for contacting us, We will contact you as soon as possible.', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('label', models.CharField(help_text='The label of the form field', verbose_name='Label', max_length=255)),
                ('field_type', models.CharField(verbose_name='Field type', max_length=16, choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')])),
                ('required', models.BooleanField(verbose_name='Required', default=True)),
                ('choices', models.CharField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='Choices', max_length=512)),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', verbose_name='Default value', max_length=255)),
                ('help_text', models.CharField(blank=True, verbose_name='Help text', max_length=255)),
                ('page', modelcluster.fields.ParentalKey(related_name='form_fields', to='home.ContactPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
