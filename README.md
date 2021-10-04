# NorenApi

Api used to connect to NorenOMS
****

## Build

to build this package and install it on your server please use 

``` pip install -r requirements.txt ```


****

## API 
class  ```NorenApi```
- [login](#md-login)
- [place_order](#md-place_order)
- [modify_order](#md-modify_order)
- [cancel_order](#md-cancel_order)
- [get_holdings](#md-get_holdings)
- [get_positions](#md-get_positions)
- [searchscrip](#md-searchscrip)
- [start_websocket](#md-start_websocket)
- [subscribe](#md-subscribe)
- [unsubscribe](#md-unsubscribe)

#### <a name="md-login"></a> login(userid, password, twoFA, vendor_code, api_secret, imei)
connect to the broker, only once this function has returned successfully can any other operations be performed

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| userid | ```string``` | False | user credentials |
| password | ```string```| False | password encrypted |
| twoFA | ```string``` | False | dob/pan |
| vendor_code | ```string``` | False | vendor code shared  |
| api_secret | ```string``` | False | your secret   |
| imei | ```string``` | False | imei identification |

#### <a name="md-place_order"></a> place_order(buy_or_sell, product_type,exchange, tradingsymbol, quantity, discloseqty, price_type, price=0.0, trigger_price=None, retention='DAY', amo='NO', remarks=None)
place an order to oms

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| buy_or_sell | ```enum``` | False | BuyorSell enum class |
| product_type | ```enum```| False | ProductType enum class |
| exchange | ```string``` | False | Exchange NSE  / NFO / BSE / CDS |
| tradingsymbol | ```string``` | False | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M |
| quantity | ```integer``` | False | order quantity   |
| discloseqty | ```integer``` | False | order disc qty |
| price_type | ```enum```| False | PriceType enum class |
| price | ```integer```| False | Price in paise, 100.00 is sent as 10000 |
| trigger_price | ```integer```| False | Price in paise |
| retention | ```string```| False | DAY / IOC / EOS |
| amo | ```string```| True | Flag for After Market Order, YES/NO  |
| remarks | ```string```| True | client order id or free text   |

#### <a name="md-modify_order"></a> modify_order(orderno, exchange, tradingsymbol, newquantity,newprice_type, newprice, newtrigger_price, amo):
modify the quantity pricetype or price of an order

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| orderno | ```string``` | False | orderno to be modified |
| exchange | ```string``` | False | Exchange NSE  / NFO / BSE / CDS |
| tradingsymbol | ```string``` | False | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M |
| newquantity | ```integer``` | False | new order quantity   |
| newprice_type | ```enum```| False | PriceType enum class |
| newprice | ```integer```| False | Price in paise, 100.00 is sent as 10000 |
| newtrigger_price | ```integer```| False | Price in paise |

#### <a name="md-cancel_order"></a> cancel_order(orderno)
cancel an order

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| orderno | ```string``` | False | orderno with status open |

#### <a name="md-get_holdings"></a> get_holdings(product_type)
retrieves the holdings as a list

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| product_type | ```enum``` | True | retreives the delivery holdings or for a given product  |

#### <a name="md-get_positions"></a> get_positions()
retrieves the positions cf and day as a list

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
|  No Parameters  |

#### <a name="md-searchscrip"></a> searchscrip(exchange, searchtext):
search for scrip or contract and its properties 

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| exchange | ```string``` | True | Exchange NSE  / NFO / BSE / CDS |
| searchtext | ```string``` | True | Search Text ie partial or complete text ex: INFY-EQ, INF.. |

the response is as follows,

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| stat | ```string``` | True | ok or Not_ok |
| values | ```string``` | True | properties of the scrip |
| emsg | ```string``` | False | Error Message |

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| exch | ```string``` | True | Exchange NSE  / NFO / BSE / CDS |
| tsym | ```string``` | True | Trading Symbol is the readable Unique id of contract/scrip |
| token | ```string``` | True | Unique Code of contract/scrip |
| pp | ```string``` | True | price precision, in case of cds its 4 ie 100.1234 |
| ti | ```string``` | True | tick size minimum increments of paise for price  |
| ls | ```string``` | True | Lot Size |

#### <a name="md-start_websocket"></a> start_websocket()
starts the websocket

| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| subscribe_callback | ```function``` | False | callback for market updates |
| order_update_callback | ```function```| False | callback for order updates |
| socket_open_callback | ```function``` | False | callback when socket is open (reconnection also) |
| socket_close_callback | ```function```| False | callback when socket is closed |

#### <a name="md-subscribe_orders"></a> subscribe_orders()
get order and trade update callbacks

#### <a name="md-subscribe"></a> subscribe([instruments])
send a list of instruments to watch
| Param | Type | Optional |Description |
| --- | --- | --- | ---|
| instruments | ```list``` | False | list of instruments [NSE|22,CDS|1] |


#### <a name="md-unsubscribe"></a> unsubscribe()
send a list of instruments to stop watch

****
## Example


```python
from NorenRestApiPy.NorenApi import PriceType, BuyorSell, ProductType
from api_helper import NorenApiPy, get_time
import logging
import hashlib

logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user        = '< user id>'
u_pwd       = '< password >'
factor2     = 'second factor'
vc          = 'vendor code'
api_secret  = 'secret key'
imei        = 'uniq identifier'

u_app_key='{0}|{1}'.format(user,api_secret)

#Convert to SHA 256 for password and app key
pwd = hashlib.sha256(u_pwd.encode('utf-8')).hexdigest()
app_key=hashlib.sha256(u_app_key.encode('utf-8')).hexdigest()

ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(ret)
```

****

## Author

Kumar Anand

****

## License

Copyright (C) 2021 Kambala Solutions Pvt Ltd- All Rights Reserved
Copying of this file, via any medium is strictly prohibited.
Proprietary and confidential.
All file transfers are logged.

****


