# -*- encoding:UTF-8 -*-
__author__ = 'wuyou'
import logging

logger = logging.getLogger(__name__)


def Switch(model_name):
    logging.debug(model_name)
    if True:
        from PowerSupply.IT6831A import Command
        return Command
