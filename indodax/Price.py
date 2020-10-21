import requests as rq
import json

class price:
  @staticmethod
  def price(coin):
    m = coin+'idr'
    url = 'https://indodax.com/api/ticker/'+m
    r = rq.get(url)
    js = json.loads(r.text)
    return js

