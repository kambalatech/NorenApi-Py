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
- [start_websocket](#markdown-header-start_websocket)
- [subscribe](#markdown-header-subscribe)
- [unsubscribe](#markdown-header-unsubscribe)

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

#### start_websocket()
starts the websocket

#### subscribe()
send a list of instruments to watch

#### unsubscribe()
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


api.subscribe('CDS|100')
api.subscribe(['NSE|22', 'BSE|522032'])

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


