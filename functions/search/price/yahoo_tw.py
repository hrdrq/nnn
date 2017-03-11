# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'https://tw.search.bid.yahoo.com/search/auction/product'

class YahooTW(object):

    def search(self, word, limit=None):
        r = requests.get(URL, params={
                'sort': 'rel',
                'acu': 1,
                'p': word,
            })
        doc = PyQuery(r.text)
        results = []
        for item in doc("div.att-item"):
            result = {}
            item = PyQuery(item)
            tag = item('div.srp-pdtaglist')('span.srp-tag')
            if tag.hasClass('bid'):
                continue
            pdcontent = item('div.srp-pdcontent')
            a = pdcontent('div.srp-pdtitle')('a')
            result['title'] = a.text()
            result['url'] = a.attr('href')
            result['img'] = item('div.srp-pdimage')('img').attr('src')
            result['price'] = int(pdcontent('div.srp-pdprice')('em.yui3-u').text().replace(',', '').replace('$', ''))
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
