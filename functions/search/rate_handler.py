# encoding: utf-8
# yahooの外貨レートAPIを使用し、日本円と台湾ドルのレートを取得
from __future__ import print_function, unicode_literals

import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def rate_handler(event):
    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22TWDJPY%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    response = requests.get(URL)
    return {'rate': float(response.json()['query']['results']['rate']['Rate'])}
