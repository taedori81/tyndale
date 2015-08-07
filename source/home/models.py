from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailforms.models import AbstractFormField, AbstractEmailForm
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    slider1_header1 = models.CharField(max_length=30,
                                       help_text='maximum length of 30 characters',
                                       default='Welcome to')
    slider1_header2 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='Tyndale international university')
    slider1_subheader1 = models.CharField(max_length=100,
                                          help_text='maximum length of 100 characters',
                                          default='The reformed theology based seminary')

    slider2_header1 = models.CharField(max_length=100,
                                       help_text='maximum length of 100 characters',
                                       default='This displays bible verse')
    slider2_subheader1 = models.CharField(max_length=30,
                                          help_text='maximum length of 30 characters',
                                          default='romans 5:8')

    main_header = models.CharField(max_length=30,
                                   help_text='maximum length of 30 characters',
                                   default='our mission')
    main_subheader = models.CharField(max_length=255,
                                      help_text='maximum length of 255 characters',
                                      default="mission's description")

    content_panels = Page.content_panels + [
        FieldPanel('slider1_header1', classname='full title'),
        FieldPanel('slider1_header2', classname='full title'),
        FieldPanel('slider1_subheader1', classname='full title'),
        FieldPanel('slider2_header1', classname='full title'),
        FieldPanel('slider2_subheader1', classname='full title'),
        FieldPanel('main_header', classname='full title'),
        FieldPanel('main_subheader', classname='full title'),
    ]


class AboutPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 750 x 300 (width x height)"
    )

    body = RichTextField(default="About Tyndale....")

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('body', classname='full')

    ]


class PresidentPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    president_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 340 x 480 (width x height)"
    )
    president_name = models.CharField(max_length=30,
                                      help_text='maximum length of 30 characters',
                                      default='President name goes here')
    president_title = models.CharField(max_length=20,
                                       help_text='maximum length of 20 characters',
                                       default='President title goes here')
    body = RichTextField(default='Welcome message of president..')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('president_image'),
        FieldPanel('president_name', classname='full'),
        FieldPanel('president_title', classname='full'),
        FieldPanel('body', classname='full'),

    ]


class ChairmanPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    chairman_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 340 x 480 (width x height)"
    )
    chairman_name = models.CharField(max_length=30,
                                      help_text='maximum length of 30 characters',
                                      default='chairman name goes here')
    chairman_title = models.CharField(max_length=20,
                                       help_text='maximum length of 20 characters',
                                       default='chairman title goes here')
    body = RichTextField(default='Welcome message of chairman..')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('chairman_image'),
        FieldPanel('chairman_name', classname='full'),
        FieldPanel('chairman_title', classname='full'),
        FieldPanel('body', classname='full'),

    ]


class MissionPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 340 x 480 (width x height)"
    )

    body = RichTextField(default='Contents of State of mission')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('body', classname='full'),

    ]


class FaithPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 340 x 480 (width x height)"
    )

    body = RichTextField(default='Contents of State of faith')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('body', classname='full'),

    ]


class StaffPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')

    first_column_header = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='header goes here')
    first_column_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 324 x 324 (width x height)"
    )

    first_column_name = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='name goes here')
    first_column_position = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='position goes here')
    first_column_spec = RichTextField(default='Spec')

    second_column_header = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='header goes here')
    second_column_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 324 x 324 (width x height)"
    )

    second_column_name = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='name goes here')
    second_column_position = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='position goes here')
    second_column_spec = RichTextField(default='Spec')

    third_column_header = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='header goes here')
    third_column_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 324 x 324 (width x height)"
    )

    third_column_name = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='name goes here')
    third_column_position = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='position goes here')

    fourth_column_header = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='header goes here')
    fourth_column_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 324 x 324 (width x height)"
    )

    fourth_column_name = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='name goes here')
    fourth_column_position = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='position goes here')

    fifth_column_header = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='header goes here')
    fifth_column_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 324 x 324 (width x height)"
    )

    fifth_column_name = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='name goes here')
    fifth_column_position = models.CharField(max_length=30,
                                           help_text='maximum length of 30 characters',
                                           default='position goes here')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),

        FieldPanel('first_column_header', classname='full'),
        ImageChooserPanel('first_column_image'),
        FieldPanel('first_column_name', classname='full'),
        FieldPanel('first_column_position', classname='full'),
        FieldPanel('first_column_spec', classname='full'),

        FieldPanel('second_column_header', classname='full'),
        ImageChooserPanel('second_column_image'),
        FieldPanel('second_column_name', classname='full'),
        FieldPanel('second_column_position', classname='full'),
        FieldPanel('second_column_spec', classname='full'),

        FieldPanel('third_column_header', classname='full'),
        ImageChooserPanel('third_column_image'),
        FieldPanel('third_column_name', classname='full'),
        FieldPanel('third_column_position', classname='full'),

        FieldPanel('fourth_column_header', classname='full'),
        ImageChooserPanel('fourth_column_image'),
        FieldPanel('fourth_column_name', classname='full'),
        FieldPanel('fourth_column_position', classname='full'),

        FieldPanel('fifth_column_header', classname='full'),
        ImageChooserPanel('fifth_column_image'),
        FieldPanel('fifth_column_name', classname='full'),
        FieldPanel('fifth_column_position', classname='full'),


    ]


class AcademicPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 750 x 300 (width x height)"
    )

    body = RichTextField(default="Academics....")

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('body', classname='full')

    ]


class AcademicProgramPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    program_title_1 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_1 = RichTextField(default="Program's Description")

    program_title_2 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_2 = RichTextField(default="Program's Description")

    program_title_3 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_3 = RichTextField(default="Program's Description")

    program_title_4 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_4 = RichTextField(default="Program's Description")

    program_title_5 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_5 = RichTextField(default="Program's Description")

    program_title_6 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_6 = RichTextField(default="Program's Description")

    program_title_7 = models.CharField(max_length=50,
                                       help_text='maximum length of 50 characters',
                                       default='academic program title goes here')
    program_body_7 = RichTextField(default="Program's Description")

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        FieldPanel('program_title_1', classname='full'),
        FieldPanel('program_body_1', classname='full'),

        FieldPanel('program_title_2', classname='full'),
        FieldPanel('program_body_2', classname='full'),

        FieldPanel('program_title_3', classname='full'),
        FieldPanel('program_body_3', classname='full'),

        FieldPanel('program_title_4', classname='full'),
        FieldPanel('program_body_4', classname='full'),

        FieldPanel('program_title_5', classname='full'),
        FieldPanel('program_body_5', classname='full'),

        FieldPanel('program_title_6', classname='full'),
        FieldPanel('program_body_6', classname='full'),

        FieldPanel('program_title_7', classname='full'),
        FieldPanel('program_body_7', classname='full'),
    ]


class FacultyPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')
    tab_title_1 = models.CharField(max_length=30,
                                   help_text='maximum length of 30 characters',
                                   default='tab title goes here')
    tab_title_2 = models.CharField(max_length=30,
                                   help_text='maximum length of 30 characters',
                                   default='tab title goes here')
    subject_name_1 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Biblical Theology / Biblical Languages')
    subject_name_2 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Hermeneutics / Christian Counseling')
    subject_name_3 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Christian Education')
    subject_name_4 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Church History/Historical Theology')
    subject_name_5 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Church Music')
    subject_name_6 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Church Ministry/Practical Theology')
    subject_name_7 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Christian Evangelism / Missiology')
    subject_name_8 = models.CharField(max_length=50,
                                   help_text='maximum length of 50 characters',
                                   default='Systematic Theology/Apologetics')

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        FieldPanel('tab_title_1', classname='full'),
        FieldPanel('tab_title_2', classname='full'),
        FieldPanel('subject_name_1', classname='full'),
        FieldPanel('subject_name_2', classname='full'),
        FieldPanel('subject_name_3', classname='full'),
        FieldPanel('subject_name_4', classname='full'),
        FieldPanel('subject_name_5', classname='full'),
        FieldPanel('subject_name_6', classname='full'),
        FieldPanel('subject_name_7', classname='full'),
        FieldPanel('subject_name_8', classname='full'),
    ]


class AdmissionPage(Page):
    subsection_title = models.CharField(max_length=30,
                                        help_text='maximum length of 30 characters',
                                        default='title goes here')
    subsection_subtitle = models.CharField(max_length=100,
                                           help_text='maximum length of 100 characters',
                                           default='subtitle goes here')

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 750 x 300 (width x height)"
    )

    body = RichTextField(default="About admission....")

    content_panels = Page.content_panels + [
        FieldPanel('subsection_title', classname='full title'),
        FieldPanel('subsection_subtitle', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('body', classname='full')

    ]


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):

    contact_header = models.CharField(max_length=30,
                                      help_text='maximum length of 30 characters',
                                      default='Contact Us')
    contact_subheader = models.CharField(max_length=100,
                                         help_text='maximum length of 100 characters',
                                         default='Fill in the form below to get in touch with us.')
    thank_you_text = models.CharField(max_length=255,
                                      help_text='maximum length of 255 characters',
                                      default='Thank you for contacting us, We will contact you as soon as possible.')

ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('contact_header', classname='full'),
    FieldPanel('contact_subheader', classname='full'),
    FieldPanel('thank_you_text', classname='full'),
    InlinePanel('form_fields', label='Form fields'),
    MultiFieldPanel([
        FieldPanel('to_address', classname='full'),
        FieldPanel('from_address', classname='full'),
        FieldPanel('subject', classname='full'),

    ], "Email")
]
