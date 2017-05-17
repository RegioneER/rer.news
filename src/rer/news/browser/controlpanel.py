# -*- coding: utf-8 -*-
from rer.news import _
from rer.news.interfaces import IRERNewsSettings  # NOQA
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm


class RERNewsSettingsEditForm(RegistryEditForm):
    """settings form."""
    schema = IRERNewsSettings
    id = 'RERNewsSettingsEditForm'
    label = _(u'RER News settings')
    description = u''


class RERNewsSettingsControlPanel(ControlPanelFormWrapper):
    """settings control panel.
    """
    form = RERNewsSettingsEditForm
