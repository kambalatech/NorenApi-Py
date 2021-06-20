# StarAPI

Api used to connect to StarUAT
****

## Build

to build this package and install it on your server please use 

``` pip install -r requirements.txt ```


****

## API 
class  ```StarApi```
- [login](#md-login)
- [place_order](#md-place_order)
- [modify_order](#md-place_order)
- [cancel_order](#md-place_order)
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
| product_type | ```string```| False | ProductType enum class |
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
from StarWebApiUAT.StarApi import StarApi 

socket_opened = False

####callbacks of client application

def event_handler_quote_update(message):
    print(message)

def open_callback():
    global socket_opened
    socket_opened = True
    print('app is connected')
    api.subscribe('CDS|100')
    api.subscribe(['NSE|22', 'BSE|522032'])

######################################################################

api = StarApi()

ret = api.login(userid = <user>, password = <pwd>, twoFA=<factor2>, vendor_code=<vc>, api_secret=<apikey>, imei=<imei>)



if ret == None:
    api.start_websocket(subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)
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


