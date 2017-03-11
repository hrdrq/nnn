# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery


class Feebee(object):
    # URL = 'https://feebee.com.tw/s/?q={word}'
    URL = 'https://feebee.com.tw/s/{word}/?mode=l&s=d'

    def search(self, word, limit=None):
        response = requests.get(self.URL.format(word=word))
        doc = PyQuery(response.text)
        # print(doc("li.fb-u"))
        results = []
        for item in doc("ol.results")("li.fb-u"):
            result = {}
            item = PyQuery(item)
            result['title'] = item('h2.large').text()
            result['price'] = [PyQuery(p).text() for p in item('div.price')('em')]
            source = item('span.source')
            if source:
                result['source'] = source.text()
            result['img'] = item('img').attr('src')
            result['url'] = item('a').eq(0).attr('href')
            if not re.search(r'^http',result['url']):
                result['url'] = 'https://feebee.com.tw' + result['url']
            # print(PyQuery(item('img')[0]).attr('src'))
            # # break
            results.append(result)
        
        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
