# encoding: utf-8
from __future__ import print_function, unicode_literals

import logging
from price.feebee import Feebee
from price.kakaku import Kakaku

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def price_handler(event):
    params = event['queryParams']
    method = event['method']
    path = event['path']

    if path == '/price/feebee':
        price = Feebee()
    elif path == '/price/kakaku':
        price = Kakaku()

    if params.get('word'):
        return price.search(params['word'])
    else:
        return {'error': True, 'message': 'The param "word" is needed.'}
