# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from rer.news import _
from z3c.form import validator
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.component import provideAdapter
from zope.interface import Interface
from zope.interface import Invalid
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRERNewsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IRERNews(model.Schema):

    directives.order_after(image='IRichText.text')
    image = RelationChoice(
        title=_(u'Image'),
        required=False,
        vocabulary='plone.app.vocabularies.Catalog',
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


class ImageValidator(validator.SimpleFieldValidator):
    """z3c.form validator class for related images
    """

    def validate(self, value):
        """Validate image
        """
        super(ImageValidator, self).validate(value)

        if not value:
            return
        if value.portal_type != 'Image':
            raise Invalid(
                _(
                    'reference_validation_image',
                    u'You can only select images.'))


class LinksValidator(validator.SimpleFieldValidator):
    """z3c.form validator class for related images
    """

    def validate(self, value):
        """Validate links
        """
        super(LinksValidator, self).validate(value)

        if not value:
            return
        invalids = filter(lambda x: x.portal_type != 'Link', value)
        if invalids:
            raise Invalid(
                _(
                    'reference_validation_image',
                    u'You can only select images.'))


# Set conditions for which fields the validator class applies
validator.WidgetValidatorDiscriminators(
    ImageValidator,
    field=IRERNews['image']
)
validator.WidgetValidatorDiscriminators(
    LinksValidator,
    field=IRERNews['related_links']
)

# Register the validator so it will be looked up by z3c.form machinery
# this should be done via ZCML
provideAdapter(ImageValidator)
provideAdapter(LinksValidator)
