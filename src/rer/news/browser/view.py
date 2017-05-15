# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from zope.i18nmessageid import MessageFactory
import pkg_resources

PLMF = MessageFactory('plonelocales')


class ERNewsView(BrowserView):
    '''
    View for ERNews
    '''

    def getVersion(self):
        return pkg_resources.get_distribution("rer.news").version

    def getEffectiveDate(self):
        """
        return a formatted date
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
