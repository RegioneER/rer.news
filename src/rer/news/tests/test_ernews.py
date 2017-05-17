# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from rer.news.interfaces import IRERNews
from rer.news.testing import RER_NEWS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ERNewsIntegrationTest(unittest.TestCase):

    layer = RER_NEWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='ERNews')
        schema = fti.lookupSchema()
        self.assertEqual(IRERNews, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='ERNews')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='ERNews')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IRERNews.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='ERNews',
            id='ERNews',
        )
        self.assertTrue(IRERNews.providedBy(obj))
