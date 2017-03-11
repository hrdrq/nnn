# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'http://auctions.search.yahoo.co.jp/search'

class YahooJP(object):

    def search(self, word, limit=None):
        r = requests.get(URL, params={
                'p': word,
                'min': 1,
                'price_type': 'bidorbuyprice',
                's1': 'score2',
                'o1': 'a',
            })
        doc = PyQuery(r.text)
        results = []
        for item in doc("div#list01")('table')('tr').not_('.la'):
            result = {}
            item = PyQuery(item)
            if not item.children('td.i'):
                continue
            # print(item.text())
            # tag = item('div.srp-pdtaglist')('span.srp-tag')
            # if tag.hasClass('bid'):
            #     continue
            # contentwrap = item('div.contentwrap')
            a = item('td.a1')('a')
            result['title'] = a.text()
            result['url'] = a.attr('href')
            result['img'] = item('td.i')('img').attr('src')
            result['price'] = int(item('td.pr2').text().replace(',', '').replace('円', ''))
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
