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


########## FISHERMAN'S TRAIL ##########

# Index Page for Fishermans Trail
class FishermanIndexPage(Page):
    template = 'blog/walking/portugal/fishermansTrail/index.html'

    banner_image = models.ForeignKey(
        'wagtailimages.image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    banner_subtitle = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        FieldPanel('banner_subtitle'),
        FieldPanel('content'),
        FieldPanel('dates'),
    ]


# Blog Page for Fishermans Trail
class FishermanBlogPage(Page):
    template = 'blog/walking/portugal/fishermansTrail/day.html'

    date = models.DateField("Post Date")
    km_walked = models.CharField(max_length=20)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    content = RichTextField(blank=True)

    cover = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    sunset = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    bed = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    route_map = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('km_walked'),
        FieldPanel('start'),
        FieldPanel('end'),
        FieldPanel('content'),
        ImageChooserPanel('cover'),
        ImageChooserPanel('sunset'),
        ImageChooserPanel('bed'),
        ImageChooserPanel('route_map'),
        MultiFieldPanel([InlinePanel("image_gallery", label="Image")],
            heading="Image Gallery",),

    ]


# Image Gallery for Fishermans Trail
class FishermanGallery(Orderable):
    page = ParentalKey("blog.FishermanBlogPage", related_name="image_gallery")
    image_gallery = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+",
        )
    panels = [ImageChooserPanel("image_gallery")]

########### CYCLING AFRICA ##########

# Index Page for Cycling Africa

# Blog Page for Cycling Africa

########## SERRA TRAMUNTANA ##########

# Index Page for Serra Tramuntana
class TramuntanaIndexPage(Page):
    template = 'blog/walking/spain/serraTramuntana/index.html'

    banner_image = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    banner_subtitle = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    content = RichTextField(blank=True)
    route_map = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')

    content_panels = Page.content_panels + [
        ImageChooserPanel('banner_image'),
        FieldPanel('banner_subtitle'),
        FieldPanel('dates'),
        FieldPanel('content'),
        ImageChooserPanel('route_map'),
    ]


# Blog Page for Fishermans Trail
class TramuntanaBlogPage(Page):
    template = 'blog/walking/spain/serraTramuntana'

    date = models.DateField("Post Date")
    km_walked = models.CharField(max_length=20)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    content = RichTextField(blank=True)

    cover = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    sunset = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    bed = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')
    route_map = models.ForeignKey('wagtailimages.image',null=True,blank=False,on_delete=models.SET_NULL,related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('km_walked'),
        FieldPanel('start'),
        FieldPanel('end'),
        FieldPanel('content'),
        ImageChooserPanel('cover'),
        ImageChooserPanel('sunset'),
        ImageChooserPanel('bed'),
        ImageChooserPanel('route_map'),
        MultiFieldPanel([InlinePanel("image_gallery", label="Image")],
            heading="Image Gallery",),

    ]


# Image Gallery for Fishermans Trail
class TramuntanaGallery(Orderable):
    page = ParentalKey("blog.TramuntanaBlogPage", related_name="image_gallery")
    image_gallery = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+",
        )
    panels = [ImageChooserPanel("image_gallery")]

# Inde

# Blog Page for Beara Way



