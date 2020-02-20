from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


# Index Page for Cycling
class CyclingIndexPage(Page):
    template =  'blog/cycling/index.html'

    # Banner
    banner_image = models.ForeignKey(
        'wagtailimages.image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_subtitle = models.CharField(max_length=200)

    # Content
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        FieldPanel('banner_subtitle'),
        FieldPanel('content'),
    ]

# Index Page for Walking
class WalkingIndexPage(Page):
    template =  'blog/walking/index.html'

    # Banner
    banner_image = models.ForeignKey(
        'wagtailimages.image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_subtitle = models.CharField(max_length=200)

    # Content
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        FieldPanel('banner_subtitle'),
        FieldPanel('content'),
    ]



# Index Page for Fishermans Trail

# Blog Page for Fishermans Trail

# Index Page for Cycling Africa

# Blog Page for Cycling Afric

# Index Page for Serra Tramuntana

# Inde

# Blog Page for Beara Way



