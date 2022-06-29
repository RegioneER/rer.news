# -*- coding: utf-8 -*-
from rer.news.interfaces import IRERNews
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(IRERNews)
class ERNews(Container):

    """Convenience subclass for ``ERNews`` portal type
    """
