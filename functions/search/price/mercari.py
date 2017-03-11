# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'https://www.mercari.com/jp/search/'

class Mercari(object):

    def search(self, word, limit=None):
        r = requests.get(URL, params={
                'keyword': word,
            })
        doc = PyQuery(r.text)
        results = []
        for item in doc("section.items-box"):
            result = {}
            item = PyQuery(item)
            result['title'] = item('h3.items-box-name').text()
            result['url'] = item('a').attr('href')
            result['img'] = item('img').attr('data-src')
            result['price'] = int(item('div.items-box-price').text().replace(',', '').replace(' ', '').replace('¥', ''))
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
