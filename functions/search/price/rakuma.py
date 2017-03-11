# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'https://api.rakuma.rakuten.co.jp/search-api/rest/product/search'

class Rakuma(object):

    def search(self, word, limit=30):
        r = requests.get(URL, params={
                'keyword': word,
                'hits': limit,

            })
        results = [
            {
                'title': item['name'],
                'img': 'http://rakuma.r10s.jp/d/strg/ctrl/25/'+item['image']+'?fit=inside%7C300%3A300',
                'price': item['price'],
                'url': 'http://rakuma.rakuten.co.jp/item/'+item['id']
            }
            for item in r.json()['productList']
        ]
        
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
