# encoding: utf-8
# 各サイトの商品値段を取得する
from __future__ import print_function, unicode_literals

import logging
from price.shopee import Shopee
from price.ruten import Ruten
from price.yahoo_tw import YahooTW
from price.yahoo_jp import YahooJP
from price.rakuma import Rakuma
from price.mercari import Mercari
from price.amazon import Amazon
from price.feebee import Feebee
from price.kakaku import Kakaku

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def price_handler(event):
    params = event['queryParams']
    method = event['method']
    path = event['path']

    platform = params.get('platform')

    if platform == 'feebee':
        price = Feebee()
    elif platform == 'kakaku':
        price = Kakaku()
    elif platform == 'shopee':
        price = Shopee()
    elif platform == 'ruten':
        price = Ruten()
    elif platform == 'yahoo_tw':
        price = YahooTW()
    elif platform == 'yahoo_jp':
        price = YahooJP()
    elif platform == 'mercari':
        price = Mercari()
    elif platform == 'rakuma':
        price = Rakuma()
    elif platform == 'amazon':
        price = Amazon()

    word = params.get('word')
    if word:
        return price.search(word, params.get('limit'))
    else:
        return {'error': True, 'message': 'The param "word" is needed.'}
