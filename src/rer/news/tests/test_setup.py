# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from rer.news.testing import RER_NEWS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that rer.news is properly installed."""

    layer = RER_NEWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rer.news is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rer.news'))

    def test_browserlayer(self):
        """Test that IRerNewsLayer is registered."""
        from rer.news.interfaces import (
            IRerNewsLayer)
        from plone.browserlayer import utils
        self.assertIn(IRerNewsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RER_NEWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rer.news'])

    def test_product_uninstalled(self):
        """Test if rer.news is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rer.news'))

    def test_browserlayer_removed(self):
        """Test that IRerNewsLayer is removed."""
        from rer.news.interfaces import \
            IRerNewsLayer
        from plone.browserlayer import utils
        self.assertNotIn(IRerNewsLayer, utils.registered_layers())
