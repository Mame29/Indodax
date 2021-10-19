import requests as rq
import time

class price:
  @staticmethod
  def price(coin):
    while True:
        try:
            m = coin+'idr'
            url = 'https://indodax.com/api/ticker/'+m
            r = rq.get(url)
            return r.json()

        except rq.exceptions.ConnectionError:
            time.sleep(5)
            continue