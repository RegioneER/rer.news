# -*- coding: utf-8 -*-
import logging


logger = logging.getLogger(__name__)


default_profile = 'profile-rer.news:default'


def to_1100(context):
    """
    """
    logger.info('Upgrading rer.news to version 1100')
    context.runImportStepFromProfile(default_profile, 'repositorytool')
    context.runImportStepFromProfile(default_profile, 'difftool')
    context.runImportStepFromProfile(default_profile, 'rolemap')


def from_1100_to_1200(context):
    """
    """
    logger.info('Upgrading rer.news from 1100 to version 1200')
    context.runImportStepFromProfile(default_profile, 'typeinfo')
