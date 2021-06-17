from StarWebApiUAT.StarApi import StarApi 
import logging
import time
logging.basicConfig(level=logging.DEBUG)

socket_opened = False

def event_handler_quote_update(message):
    #e   Exchange
    #tk  Token
    #lp  LTP
    #pc  Percentage change
    #v   volume
    #o   Open price
    #h   High price
    #l   Low price
    #c   Close price
    #ap  Average trade price

    print(message)
    

 

def open_callback():
    global socket_opened
    socket_opened = True
    print('app is connected')
    api.subscribe('NSE|22')
    api.subscribe(['NSE|22', 'BSE|522032'])



api = StarApi()

user    = <uid>
pwd     = <password>
factor2 = <2nd factor>
vc      = <vendor code>
apikey  = <secret key>
imei    = <imei>

ret = api.login(userid = user, password = pwd, twoFA=factor2, vendor_code=vc, api_secret=apikey, imei=imei)



if ret != None:
    api.start_websocket(subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)

    while True:
        time.sleep(1)
        pass