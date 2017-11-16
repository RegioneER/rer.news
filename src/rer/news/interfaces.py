# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from rer.news import _
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRERNewsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRERNews(model.Schema):

    directives.order_after(image='IRichText.text')
    image = RelationChoice(
        title=_(u'Image'),
        required=False,
        source=CatalogSource(portal_type=('Image')),
    )
    directives.widget(
        'image',
        RelatedItemsFieldWidget,
        source=CatalogSource(portal_type=('Image'))
    )

    directives.order_after(image_caption='image')
    image_caption = schema.TextLine(
        title=_(u'label_image_caption', default=u'Image Caption'),
        description=u'',
        required=False,
    )

    directives.order_after(related_links='image_caption')
    related_links = RelationList(
        title=_(u'Related links'),
        default=[],
        value_type=RelationChoice(
            title=u'Related',
            source=CatalogSource(portal_type=('Link')),
        ),
        required=False
    )
    directives.widget(
        'related_links',
        RelatedItemsFieldWidget,
        source=CatalogSource(portal_type=('Link'))
    )


class IRERNewsSettings(Interface):
    news_archive = schema.TextLine(
        title=_(u'label_news_archive', default=u'News archive'),
        description=_(
            u'label_image_caption_help',
            default=u'Insert the path to a news arcvhive folder.'),
        required=True)
