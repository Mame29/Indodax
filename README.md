# Indodax
[PyPI version 1.0](https://pypi.org/project/indodax/1.0/)
Modul ini untuk trading di indodax

# Install
```sh
pip install indodax
```
# Cara Penggunaan
  ## melihat harga

  ```sh
  $ python
  Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
  [GCC 9.3.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> from indodax.Indodax import indodax
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
  
  ## Melihat Order yang Baru/Di Tahan
  ```idr_or_btc``` adalah variable dimana anda membeli/menjual dengan BTC atau IDR pilihannya hanya 2 saja, tetapi default   adalah IDR. jika anda membeli/menjual dengan IDR maka ```idr_or_btc``` abaikan saja.
  ```sh
  >>> a.open_order('btc', idr_or_btc='idr') # Contoh saya membeli BTC, disini anda akn melihat order id anda
  ...
  ```

  ## Melihat riwayat order
  ```sh
  >>> a.order_history('btc') # Anggap saja semua order terlihat
  ...
  ```
  ## Trade Buy/Sell
  Pemanggilan fungsi trade, fungsi trade ada 2 yaitu ```trade_buy(coin, diharga, jumlah, idr_or_btc='idr')``` dan ```trade_sell(coin, diharga, jumlah, idr_or_btc='idr')```. variable ```coin``` adalah jenis qurency, variable ```diharga``` adalah harga qurency-nya, variable ```jumlah``` adalah anda nilai pembelian/penjualan, ```idr_or_btc='idr'``` abaikan jika IDR
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
  

Jika anda suka dengan modul ini anda bisa donasi di:
DOGECOIN: D7rzpq91xmUVkER6E1ndfinRjRS4jvBkgV
LTC     : M9nQQZXwHQaoNStJrBcr6UfdCqx2RJHz5e
