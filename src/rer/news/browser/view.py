# -*- coding: utf-8 -*-
from plone import api
from plone.api.exc import InvalidParameterError
from Products.Five.browser import BrowserView
from rer.news.interfaces import IRERNewsSettings
from zope.i18nmessageid import MessageFactory
import logging
import pkg_resources

logger = logging.getLogger(__name__)
PLMF = MessageFactory('plonelocales')


class ERNewsView(BrowserView):
    '''
    View for ERNews
    '''

    def getVersion(self):
        return pkg_resources.get_distribution("rer.news").version

    def getEffectiveDate(self):
        """
        return infos to format date
        """
        effective = self.context.effective()
        if effective.year() == 1969:
            # not yet published
            return {}
        return {
            'weekday': u'weekday_{0}'.format(effective.aDay().lower()),
            'month': u'month_{0}'.format(effective.aMonth().lower()),
            'day': effective.day(),
            'year': effective.year()
        }

    def getNewsContents(self):
        return self.context.getFolderContents()

    def getLinks(self):
        links = getattr(self.context, 'related_links', [])
        if not links:
            return []
        return [x.to_object for x in links if self.canAccessLink(x)]

    def canAccessLink(self, ref):
        """
        check if the reference is available for the current user or isn't a
        broken reference.
        """
        if ref.isBroken():
            return False
        link = ref.to_object
        return api.user.has_permission(
            'View',
            user=api.user.get_current(),
            obj=link)

    def getNewsArchiveLink(self):
        try:
            path = api.portal.get_registry_record(
                'news_archive',
                interface=IRERNewsSettings)
        except InvalidParameterError as e:
            logger.exception(e)
            return ""
        if not path:
            return ""
        item = api.content.get(path=path)
        if not item:
            return ""
        return item.absolute_url()
