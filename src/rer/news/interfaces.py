# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.app.vocabularies.catalog import CatalogSource
from rer.news import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.autoform import directives as form
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget


class IRerNewsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IERNews(Interface):

    image = RelationList(
        title=_(u'Image'),
        default=[],
        max_length=1,
        value_type=RelationChoice(
            title=u"Related",
            source=CatalogSource(portal_type=('Image')),
        ),
        required=False
    )
    form.widget(
        'image',
        RelatedItemsFieldWidget,
        source=CatalogSource(portal_type=('Image'))
    )

    image_caption = schema.TextLine(
        title=_(u'label_image_caption', default=u'Image Caption'),
        description=u'',
        required=False,
    )

    related_links = RelationList(
        title=_(u'Related links'),
        default=[],
        value_type=RelationChoice(
            title=u"Related",
            source=CatalogSource(portal_type=('Link')),
        ),
        required=False
    )
    form.widget(
        'related_links',
        RelatedItemsFieldWidget,
        source=CatalogSource(portal_type=('Link'))
    )
