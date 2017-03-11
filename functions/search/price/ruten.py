# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'http://search.ruten.com.tw/search/s000.php'

class Ruten(object):

    def search(self, word, limit=None):
        r = requests.get(URL, params={
                'enc': 'u',
                'searchfrom': 'indexbar',
                'k': word,
                't': 0
            })
        r.encoding = r.apparent_encoding
        doc = PyQuery(r.text)
        results = []
        for item in doc("div.rt-store-goods-disp-mix"):
            result = {}
            item = PyQuery(item)
            body = item('div.media-body')
            a = body('a.item-name-anchor')
            result['title'] = a.text()
            result['url'] = a.attr('href')
            result['img'] = item('div.media-img')('img').attr('src')
            result['price'] = int(body('td.item-content-direct-price')('strong.rt-text-price').text().replace(',', ''))
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
