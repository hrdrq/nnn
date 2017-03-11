# encoding: utf-8
from __future__ import print_function, unicode_literals

import requests
import re
from pyquery import PyQuery


class Kakaku(object):
    URL = "http://s.kakaku.com/search_results/{word}/"

    UA = ("Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0_1 like Mac OS X; ja-jp) "
          "AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5B108 "
          "Safari/525.20")

    def search(self, word, limit=None):
        response = requests.get(self.URL.format(word=word), headers={'User-Agent': self.UA})
        doc = PyQuery(response.text)

        rows = []
        for item in doc("ul.linkList").eq(0)("li"):
            item = PyQuery(item)
            info = item("dl.productInfo")
            maker = info("p.txt12").text()
            if not maker:
                continue

            price = re.sub(u"[¥〜,]", "", info("dd").text())
            if not price:
                continue
            price = int(price)

            url = item("a").attr("href").replace("/s.", "/")
            url = "%s%s" % (url, "pricehistory/")
            image_url = item("div.image img").attr("src")
            # if image_url:
            #     image_url=self.PROXY_WRAPPER_URL % (options.proxy_host,
            #                                         url_escape(image_url))

            publish_str = item("li.date").text()
            if publish_str:
                publish_str = publish_str.split(" ")[0]

            rating = item("span.reviewIcon span").text()
            rating_cls = item("span.reviewIcon span").attr("class")
            if rating:
                rating = float(rating.split(" ")[1])

            lank = item("span.rankIcon").text()
            kuchikomi = item("span.kuchikomiIcon").text()

            review = None
            m = re.search(u'（(.+)）', item("ul.reviews").text())
            if m:
                review = m.group(1)

            rows += [{"title": info("dt").text(),
                      "url": url,
                      "price": price,
                      "image_url": image_url,
                      "publish_str": publish_str,
                      "rating": rating,
                      "rating_cls": rating_cls,
                      "lank": lank,
                      "kuchikomi": kuchikomi,
                      "review": review}]

        return {
            "rows": rows, "has_next": False,
        }
