# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rer.news


class RerNewsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rer.news)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rer.news:default')


RER_NEWS_FIXTURE = RerNewsLayer()


RER_NEWS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RER_NEWS_FIXTURE,),
    name='RerNewsLayer:IntegrationTesting'
)


RER_NEWS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RER_NEWS_FIXTURE,),
    name='RerNewsLayer:FunctionalTesting'
)


RER_NEWS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RER_NEWS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='RerNewsLayer:AcceptanceTesting'
)
