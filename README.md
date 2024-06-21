# Indodax
[PyPI version 1.3.2](https://pypi.org/project/indodax/1.3.2/)
Modul ini untuk trading di indodax

# Install
```sh
pip install indodax
```
# Cara Penggunaan
  ## Melihat Harga

  ```sh
  $ python
  Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
  [GCC 9.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> from indodax import indodax
  >>> indodax.get_price('btc') #contoh melihat harga BTC
  {'ticker': {'high': '186608000', 'low': '173463000', 'vol_btc': '277.39109788', 'vol_idr': '49592483275', 'last':   '186306000', 'buy': '186305000', 'sell': '186306000', 'server_time': 1603298398}}
  ```
  
  ## Melihat Info Saldo
  pertama anda harus mengambil key dan secret di akun anda, jika sudah ada silahkan ikuti instruksi ini sebagai langkah awal:

  ```sh
  >>> key = 'YOUR_KEY'
  >>> secret = b'YOUR_SECRET'
  >>> a = indodax(key, secret)
  >>> a.get_info() # anggap saja ini adalah informasi saldo dan alamat qurenncy anda
  { "succses": '1',
  ...
  ```
  
  ## Melihat History
  ```sh
  >>> a.history() # Anggap saja history anda sudah ada
  ...
  ```
  
  ## Melihat Order Baru/Di Tahan
  ```idr_or_btc``` adalah variable dimana anda membeli/menjual dengan BTC atau IDR pilihannya hanya 2 saja, tetapi default   adalah IDR. jika anda membeli/menjual dengan IDR maka ```idr_or_btc``` abaikan saja.
  ```sh
  >>> a.open_order('btc', idr_or_btc='idr') # Contoh saya membeli BTC, disini anda akn melihat order id anda
  ...
  ```

  ## Melihat Riwayat Order
  ```sh
  >>> a.order_history('btc') # Anggap saja semua order terlihat
  ...
  ```
  ## Trade Buy/Sell
  Pemanggilan fungsi trade, fungsi trade ada 2 yaitu ```trade_buy(coin, diharga, jumlah, idr_or_btc='idr')``` dan ```trade_sell(coin, diharga, jumlah, idr_or_btc='idr')```. variable ```coin``` adalah jenis qurency, variable ```diharga``` adalah harga qurency-nya, variable ```jumlah``` adalah nilai pembelian/penjualan, ```idr_or_btc='idr'``` abaikan jika IDR
   ### Buy
    
   ```sh
   >>> a.trade_buy('btc', '186306000', '50000') # ini jika anda membeli dengan IDR
   ...
   ```
    
   ### Sell
    
   ```sh
   >>> a.trade_sell('btc', '190000000', '0.005') # anggap saja saya menjual BTC di harga 190Juta
   ...
   ```
  ## Instan Order
  instan_trade(coin, jumlah, type) digunakan untuk order secara instan.
  cara penggunaan `instan_trade("trx", 10000, 'buy or sell')`

  ## Cancel Order
  Disini menggunakan 2 fungsi yaitu ```cancel_order_buy(coin, order_id, idr_or_btc='idr')``` dan ```cancel_order_sell(coin, order_id, idr_or_btc='idr')```. ```order_id``` dari ```open_order(...)```.
  
   ### Buy
   ```sh
   >>> a.cancel_order_buy('btc', '12345') # Kalau order id-nya benar, akan ada result succses = 1
   ...
   ```
   
   ### Sell
   ```sh
   >>> a.cancel_order_sell('btc', '12345') # Hampir sama dengan Buy, tapi tergantung type pembelian atau penjualan
   ...
   ```
   
  ## Withdraw
  fungsi withdraw ```withdraw(coin, address, amount, memo='', req_id='')```. Fungsi ini membutuhkan urlcallback agar dapat bekerja dengan baik.
  
  ```sh
  >>> a.withdraw('doge', 'D7rzpq91xmUVkER6E1ndfinRjRS4jvBkgV', '100') # memo hanya untuk address yg menggunakan memo
  ...
  ```
  
# Donate
Jika anda suka dengan modul ini anda bisa donasi di bawah ini

BTC    : 3BqqfUGaARBBCkMN6w6nV7hYjikvac3dJ4

BCHABC : qzdt37fmnftrm8xr50vxza640f48sfnlyqlsfjpyzk

DOGE   : D7rzpq91xmUVkER6E1ndfinRjRS4jvBkgV

LTC    : M9nQQZXwHQaoNStJrBcr6UfdCqx2RJHz5e
