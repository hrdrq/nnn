# encoding: utf-8
from __future__ import print_function, unicode_literals
import json
import urllib

from main import handle
from price.shopee import Shopee
from price.ruten import Ruten
from price.yahoo_tw import YahooTW
from price.yahoo_jp import YahooJP
from price.rakuma import Rakuma
from price.mercari import Mercari
from price.amazon import Amazon
from price.feebee import Feebee
from price.kakaku import Kakaku

def feebee_test(word):
    feebee = Feebee()
    return feebee.search(word)

def shopee_test(word):
    shopee = Shopee()
    return shopee.search(word)

def ruten_test(word):
    ruten = Ruten()
    return ruten.search(word)

def yahoo_tw_test(word):
    yahoo_tw = YahooTW()
    return yahoo_tw.search(word)

def yahoo_jp_test(word):
    yahoo_jp = YahooJP()
    return yahoo_jp.search(word)

def rakuma_test(word):
    rakuma = Rakuma()
    return rakuma.search(word)

def mercari_test(word):
    mercari = Mercari()
    return mercari.search(word)

def amazon_test(word):
    amazon = Amazon()
    return amazon.search(word)

def kakaku_test(word):
    kakaku = Kakaku()
    return kakaku.search(word)

def main_test():
    data = {
        'method': 'GET',
        'headers': {
            'content-type': 'application/json',
        },
        'path': '/price',
        'queryParams': {
            "word": "PowerShot G7",
            "platform": 'shopee'
        },
        'body': {
        }
    }
    return handle(data, None)

if __name__ == '__main__':

    res = yahoo_tw_test('PowerShot G7')
    # res = main_test()
    print(json.dumps(res, indent=4, ensure_ascii=False))
