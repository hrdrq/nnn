# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re

SEARCH_URL = "https://shopee.tw/api/v1/search_items"
ITEMS_URL = 'https://shopee.tw/api/v1/items/'

class Shopee(object):

    def search(self, word, limit=30):
        res = requests.get(SEARCH_URL, params={
                'keyword': word,
                'by': 'pop',
                'order': 'desc',
                'limit': limit,
                'skip_price_adjust': False,
            }).json()
        item_shop_ids = res['items']
        csrftoken = '14L0NtB3VIi7MgbUvRKP0Omm4di7UeR2' #なんの文字列でも大丈夫らしい
        headers = {
            'Cookie':'csrftoken='+csrftoken,
            'Referer':'https://shopee.tw',
            'x-csrftoken':csrftoken
        }
        res = requests.post(ITEMS_URL, json={'item_shop_ids':item_shop_ids}, headers=headers).json()
        results = []
        for item in res:
            result = {}
            result['img'] = 'https://cfshopeetw-a.akamaihd.net/file/{}_tn'.format(item['image'])
            result['title'] = item['name']
            result['url'] = 'https://shopee.tw/{}-i.{}.{}'.format(item['name'], item['shopid'], item['itemid'])
            result['price'] = item['price']/100000
            price_max = item.get('price_max', -1)
            if price_max != -1 and price_max != item['price']:
                result['price_max'] = price_max/100000
            results.append(result)

        if results:
            return {"status": 'success', "results": results}
        else:
            return {"status": 'error', "error_detail": "Nothing found."}
