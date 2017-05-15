# -*- coding: utf-8 -*-
from interfaces import IERNews
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IERNews)
class ERNews(Container):

    """Convenience subclass for ``ERNews`` portal type
    """
