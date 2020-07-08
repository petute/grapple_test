from django.db import models

from wagtail.core.models import Page
from wagtail.core import fields
from wagtail.core import blocks
from wagtail.documents import blocks as docblocks
from wagtail.images import blocks as imgblocks
from wagtail.snippets import blocks as snipblocks
from wagtail.embeds import blocks as embedsblocks
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.snippets.models import register_snippet

from grapple.models import (
    GraphQLInt,
    GraphQLBoolean,
    GraphQLString,
    GraphQLFloat,
    GraphQLImage,
    GraphQLDocument,
    GraphQLSnippet,
    GraphQLEmbed,
    GraphQLStreamfield,
)
from grapple.helpers import register_streamfield_block

#Snippets

@register_snippet
class Snippet(models.Model):
    url = models.URLField()


#Headers

@register_streamfield_block
class _H_BannerBlock(blocks.StructBlock):
    autofield = models.AutoField()
    bigautofield = models.BigAutoField()
    bigintegerfield = models.BigIntegerField()
    binaryfield = models.BinaryField()

    graphql_fields = [
        GraphQLInt("autofield"),
        GraphQLInt("bigautofield"),
        GraphQLInt("bigintegerfield"),
        GraphQLInt("binaryfield"),
    ]

    
@register_streamfield_block
class _H_HeadLineBlock(blocks.StructBlock):
    booleanfield = models.BooleanField()
    charfield = models.CharField()
    datefield = models.DateField()
    datetimefield = models.DateTimeField()

    graphql_fields = [
        GraphQLBoolean("booleanfield"),
        GraphQLString("charfield"),
        GraphQLString("datefield"),
        GraphQLString("datetimefield"),
    ]

#Sections

@register_streamfield_block
class _S_MainSectionBlock(blocks.StructBlock):
    decimalfield = models.DecimalField()
    durationfield = models.DurationField()
    emailfield = models.EmailField()
    filefield = models.FileField()
    filepathfield = models.FilePathField()

    graphql_fields = [
        GraphQLFloat("decimalfield"),
        GraphQLString("durationfield"),
        GraphQLString("emailfield"),
        # Dunno what Grapple Model to use for file type
        GraphQLString("filepathfield"),
    ]


@register_streamfield_block
class _S_SideSectionBlock(blocks.StructBlock):
    floatfield = models.FloatField()
    imagefield = models.ImageField()
    integerfield = models.IntegerField()
    genericipaddressfield = models.GenericIPAddressField()
    nullbooleanfield = models.NullBooleanField()

    graphql_fields = [
        GraphQLFloat("floatfield"),
        GraphQLImage("imagefield"),
        GraphQLInt("integerfield"),
        GraphQLString("genericipaddressfield"),
        GraphQLBoolean("nullbooleanfield"),
    ]


@register_streamfield_block
class _S_CoffeBlock(blocks.StructBlock):
    positiveintegerfield = models.PositiveIntegerField()
    positivesmallintegerfield = models.SmallIntegerField()
    slugfield = models.SlugField()
#   smallautofield = models.SmallAutoField()
    smallintegerfield = models.SmallIntegerField()
    textfield = models.TextField()

    graphql_fields = [
        GraphQLInt("positiveintegerfield"),
        GraphQLString("slugfield"),
        GraphQLInt("smallintegerfield"),
        GraphQLString("textfield"),
    ]


@register_streamfield_block
class _S_SmallBlock(blocks.StructBlock):
    timefield = models.TimeField()
    urlfield = models.URLField()
    uuidfield = models.UUIDField()
    charblock = blocks.CharBlock()
    textblock = blocks.TextBlock()
    emailblock = blocks.EmailBlock()

    graphql_fields = [
        GraphQLString("timefield"),
        GraphQLString("urlfield"),
        GraphQLString("uuidfield"),
        GraphQLString("charblock"),
        GraphQLString("textblock"),
        GraphQLString("emailblock"),
    ]


@register_streamfield_block
class _S_BigBlock(blocks.StructBlock):
    integerblock = blocks.IntegerBlock()
    floatblock = blocks.FloatBlock()
    decimalblock = blocks.DecimalBlock()
    regexblock = blocks.RegexBlock(regex='')
    urlblock = blocks.URLBlock()
    booleanblock = blocks.BooleanBlock()
    dateblock = blocks.DateBlock()

    graphql_fields = [
        GraphQLInt("integerblock"),
        GraphQLFloat("floatblock"),
        GraphQLFloat("decimalblock"),
        GraphQLString("regexblock"),
        GraphQLString("urlblock"),
        GraphQLBoolean("booleanblock"),
        GraphQLString("dateblock"),
    ]

@register_streamfield_block
class _S_TallBlock(blocks.StructBlock):
    timeblock = blocks.TimeBlock()
    datetimeblock = blocks.DateTimeBlock()
    richtextblock = blocks.RichTextBlock()
    rawhtmlblock = blocks.RawHTMLBlock()
    blockquoteblock = blocks.BlockQuoteBlock()
#??  choiceblock = blocks.ChoiceBlock()
#    multiplechoiceblock = blocks.MultipleChoiceBlock()
#??  pagechooserblock = blocks.PageChooserBlock()

    graphql_fields = [
        GraphQLString("timeblock"),
        GraphQLString("datetimeblock"),
        GraphQLString("richtextblock"),
        GraphQLString("rawhtmlblock"),
        GraphQLString("blockquoteblock"),
        #GraphQLString("choiceblock"), #??
        #dunno what to use for the pagechooserblock
    ]

@register_streamfield_block
class _S_LightBlock(blocks.StructBlock):
    documentchooserblock = docblocks.DocumentChooserBlock()
    imagechooserblock = imgblocks.ImageChooserBlock()
    snippetchooserblock = snipblocks.SnippetChooserBlock(target_model='home.Snippet')
    embedblock = embedsblocks.EmbedBlock()
    staticblock = blocks.StaticBlock()

    graphql_fields = [
        GraphQLDocument("documentchooserblock"), #??
        GraphQLImage("imagechooserblock"), #??
        GraphQLSnippet("snippetchooserblock", snippet_model='home.Snippet'), #??
        GraphQLEmbed("embedblock"),
        GraphQLString("staticblock"),
    ]

    

#Pages
class HomePage(Page):
    headers = fields.StreamField([
        ('h_bannerblock', _H_BannerBlock()),
        ('h_headlineblock', _H_HeadLineBlock()),
    ], null=True, blank=False)
    sections = fields.StreamField([
        ('s_mainsection', _S_MainSectionBlock()),
        ('s_sidesection', _S_SideSectionBlock()),
        ('s_coffeblock', _S_CoffeBlock()),
        ('s_smallblock', _S_SmallBlock()),
        ('s_bigblock', _S_BigBlock()),
        ('s_tallblock', _S_TallBlock()),
        ('s_lightblock', _S_LightBlock()),
    ], null=True, blank=False)

    main_content_panels = [
      StreamFieldPanel('headers'),
      StreamFieldPanel('sections')
    ]

    graphql_fields = [
        GraphQLStreamfield("headers"),
        GraphQLStreamfield("sections"),
    ]

    content_panels = Page.content_panels + main_content_panels

