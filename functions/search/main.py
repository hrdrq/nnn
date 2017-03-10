# encoding: utf-8
from __future__ import print_function, unicode_literals

import logging
from price_handler import price_handler
from rate_handler import rate_handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    """
    Lambda handler
    """
    path = event['path']
    if path.find('/price') != -1:
        return price_handler(event)
    elif path.find('/rate') != -1:
        return rate_handler(event)
