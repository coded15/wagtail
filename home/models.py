import imp
from pyexpat import features
from tabnanny import verbose
from turtle import home
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField


class HomePage(Page):
    """Home page model."""
    templates = "templates/home/home_page.html"
    max_count = 1

    content = StreamField(
        [
            ("cta", blocks.CTABlock())
        ],
        null=True,
        blank=True
    )

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels+[
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        StreamFieldPanel("content"),

    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
