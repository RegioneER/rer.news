# -*- coding: utf-8 -*-
from plone.app.dexterity import _
# from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
# from plone.supermodel import model
# from z3c.form.interfaces import IAddForm
# from z3c.form.interfaces import IEditForm
from zope import schema
from zope.interface import provider
from plone.app.dexterity.behaviors.metadata import IBasic, Basic
from plone.directives import form


@provider(IFormFieldProvider)
class IBasicRerNews(IBasic):
    title = schema.Text(
        title=_(u'label_title', default=u'Title'),
        required=True
    )
    form.widget('title', rows=2)


class BasicRerNews(Basic):
    """
    Basic methods to store title and description
    """
