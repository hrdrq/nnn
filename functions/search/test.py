# encoding: utf-8
from __future__ import print_function, unicode_literals
import json

from main import handler
from price.feebee import Feebee
from price.kakaku import Kakaku

def feebee_test():
    feebee = Feebee()
    return feebee.search('PowerShot G7')

def kakaku_test():
    kakaku = Kakaku()
    return kakaku.search('PowerShot G7')

def main_test():
    data = {
        'method': 'GET',
        'headers': {
            'content-type': 'application/json',
        },
        'path': '/price/feebee',
        'queryParams': {
            "word": "PowerShot G7"
        },
        'body': {
        }
    }
    return handle(data, None)

if __name__ == '__main__':

    # res = feebee_test()
    # res = kakaku_test()
    res = main_test()
    print(json.dumps(res, indent=4, ensure_ascii=False))
