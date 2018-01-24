# -*- coding: utf-8 -*-
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import ILocalPortletAssignmentManager
from plone.portlets.interfaces import IPortletManager
from zope.component import getMultiAdapter
from zope.component import getUtility


def disablePortlets(news, event):
    """
    disable portlets inheritance
    """
    for manager in ['plone.leftcolumn', 'plone.rightcolumn']:
        portletManager = getUtility(IPortletManager, name=manager)
        assignable = getMultiAdapter(
            (news, portletManager),
            ILocalPortletAssignmentManager)
        assignable.setBlacklistStatus(
            CONTEXT_CATEGORY,
            True)
