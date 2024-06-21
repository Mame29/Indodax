import json,time,urllib
import requests as c
from hmac import HMAC
from indodax.Price import price

__version__ = '1.3.2'

class indodax:
  '''Ini dirancang agar mempermudah jual beli mata uang digital di indodax ambil key dan secret di akun anda
  >>> from Indodax import indodax
  >>> key = 'ABCD-EFGH-IJKL-MNOP' # Ambil dari akun indodax anda
  >>> secret = b'hiwiwijwjsjsjsj' # Ini jg sama
  >>> a = indodax(key, secret)
  >>> a.get_info() # Nanti akan muncul informasi saldo
  '''


  def __init__(self, key, secret):
    #key dari indodax
    self.key = key
    #secret dari indodax
    self.secret = secret


  def query(self, method, **kwargs: dict) -> dict:
    url = 'https://indodax.com/tapi/'

    kwargs['method'] = method
    kwargs['nonce'] = int(time.time()*1000000)

    sign = HMAC(self.secret, urllib.parse.urlencode(kwargs).encode('utf-8'), 'sha512').hexdigest()
    headers = {
      'Sign': sign,
      'Key': self.key
    }

    s = c.Session()
    r = s.post(url, headers=headers, data=kwargs)
    # js = json.dumps(json.loads(r.text), sort_keys=False, indent=4)
    return r.json()

  @staticmethod
  def get_price(coin):
    a = price.price(coin)
    return a


  def get_info(self):
    return self.query('getInfo')


  def history(self):
    return self.query('transHistory')


  def trade_buy(self, coin, diharga, jumlah, idr_or_btc='idr'):
    ''' lanjutan intruksi di atas
    >>> a.trade_buy('doge', '41', '50000') # kita akan membeli doge 50rb

    '''
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'type': 'buy',
      'price': diharga,
      idr_or_btc: jumlah,
    }

    return self.query('trade', **m)


  def trade_sell(self, coin, diharga, jumlah, idr_or_btc='idr'):
    ''' disini sama cara penggunaanya seperti trade_buy()
    hanya saja ini untuk menjual
    '''
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'type': 'sell',
      'price': diharga,
      coin: jumlah
    }

    return self.query('trade', **m)


  def open_order(self,coin, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair
    }

    return self.query('openOrders', **m)


  def order_history(self, coin, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {'pair': pair}

    return self.query('orderHistory', **m)


  def get_order(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id
    }

    return self.query('getOrder', **m)


  def instan_trade(self, coin, jumlah, type: str):
      '''instan_trade(coin, jumlah, type) digunakan untuk order secara instan.
      cara penggunaan `instan_trade("trx", 10000, 'buy or sell')`'''
      jk = indodax.get_price(coin)
      jk = jk['ticker']
      buy = jk['buy']
      sell = jk['sell']
      if type == 'buy':
          return self.trade_buy(coin, buy, jumlah)

      if type == 'sell':
          return self.trade_sell(coin, sell, jumlah)

  def cancel_order_buy(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id,
      'type': 'buy'
    }
    return self.query('cancelOrder', **m)


  def cancel_order_sell(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id,
      'type': 'sell'
    }

    return self.query('cancelOrder', **m)


  def withdraw(self, coin, address, amount, memo='', req_id=''):
    '''Hati2 dengan ini, jika anda salah maka coin kalian akan hilang
    '''
    m = {
      'currency': coin,
      'withdraw_address': address,
      'withdraw_amount': amount,
      'withdraw_memo': memo,
      'request_id': req_id
    }

    return self.query('withdrawCoin', **m)
