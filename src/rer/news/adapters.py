# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.syndication.adapters import DexterityItem
from Products.CMFPlone.interfaces.syndication import IFeed
from rer.news.interfaces import IRERNews
from zope.component import adapter


@adapter(IRERNews, IFeed)
class SyndicationERNewsItem(DexterityItem):

    def __init__(self, context, feed):
        super(SyndicationERNewsItem, self).__init__(context, feed)
        image_ref = getattr(self.context, 'image', None)
        if not image_ref:
            return
        image = image_ref.to_object
        if not image:
            return
        image_file = getattr(image, 'image', None)
        if not image_file:
            return
        self.file = image_file
        self.field_name = 'image'
