# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery

URL = 'https://www.amazon.co.jp/s'
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")


class Amazon(object):

    def search(self, word, limit=None):
        r = requests.get(URL, 
            params={
                'field-keywords': word,
            }, 
            headers={
                'User-Agent': UA
            })
        doc = PyQuery(r.text)
        results = []
        for item in doc("li.s-result-item"):
            result = {}
            item = PyQuery(item)
            price = item('span.s-price')
            if not price:
                continue
            a = item('a.s-access-detail-page')
            result['title'] = a.text()
            result['url'] = 'https://www.amazon.co.jp'+a.attr('href')
            result['img'] = item('img').attr('src')
            result['price'] = int(price.text().replace(',', '').replace(' ', '').replace('￥', ''))
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
